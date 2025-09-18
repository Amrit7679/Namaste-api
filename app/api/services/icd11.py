import httpx
import logging
from typing import List

from app.api.models.common import ICD11Term
from app.core.config import settings
from fastapi import HTTPException

logger = logging.getLogger(__name__)

class ICD11Service:
    def __init__(self):
        self.base_url = settings.ICD11_BASE_URL  # e.g. https://id.who.int/icd/release/11/2024-01
        self.token = None
        self.token_expiry = None

    async def get_access_token(self):
        """Get OAuth2 token for ICD-11 API"""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    "https://icdaccessmanagement.who.int/connect/token",
                    data={
                        "client_id": settings.ICD11_CLIENT_ID,
                        "client_secret": settings.ICD11_CLIENT_SECRET,
                        "scope": "icdapi_access",
                        "grant_type": "client_credentials"
                    }
                )
                response.raise_for_status()
                data = response.json()
                self.token = data["access_token"]
                logger.info("✅ Successfully obtained ICD-11 access token.")
                return self.token
        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP error obtaining ICD-11 token: {e.response.status_code} - {e.response.text}")
            raise HTTPException(status_code=500, detail="Failed to authenticate with ICD-11 API")
        except Exception as e:
            logger.error(f"Error obtaining ICD-11 access token: {e}")
            raise HTTPException(status_code=500, detail="Failed to authenticate with ICD-11 API")

    async def search_icd11(self, query: str, use_flexisearch: bool = True) -> List[ICD11Term]:
        """Search ICD-11 for matching terms (with debug raw response)"""
        if not self.token:
            await self.get_access_token()

        headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "API-Version": "v2",
            "Accept-Language": "en"
        }

        search_endpoint = "flexisearch" if use_flexisearch else "search"
        url = f"{self.base_url}/{search_endpoint}"

        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    url,
                    params={"q": query},
                    headers=headers
                )
                response.raise_for_status()
                data = response.json()

                # 🔹 Debug: return raw JSON for now
                logger.debug(f"ICD-11 raw JSON: {data}")

                results = []

                # Try different response structures
                entities = (
                    data.get("destinationEntities")
                    or data.get("results")
                    or data.get("@graph")
                    or []
                )

                for item in entities:
                    results.append(ICD11Term(
                        uri=item.get("id", ""),
                        code=item.get("theCode", ""),
                        title=(item.get("title", {}).get("@value") if isinstance(item.get("title"), dict) else str(item.get("title"))),
                        definition=(item.get("definition", {}).get("@value") if isinstance(item.get("definition"), dict) else str(item.get("definition"))),
                        parent=item.get("parent", []),
                        children=item.get("child", []),
                        synonyms=[s.get("@value", "") for s in item.get("synonym", [])] if item.get("synonym") else []
                    ))

                if not results:
                    # fallback: return raw response inside a dummy ICD11Term
                    return [ICD11Term(
                        uri="raw",
                        code="raw",
                        title=str(data),
                        definition="(raw dump)",
                        parent=[],
                        children=[],
                        synonyms=[]
                    )]

                logger.info(f"✅ Found {len(results)} ICD-11 matches for query: '{query}'")
                return results

        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP error searching ICD-11 for '{query}': {e.response.status_code} - {e.response.text}")
            return []
        except Exception as e:
            logger.error(f"Error searching ICD-11 for '{query}': {e}")
            return []
