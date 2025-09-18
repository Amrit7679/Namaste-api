import json
import logging
from typing import List, Optional, Dict, Any

from app.api.models.common import NAMASTETerm
from app.core.config import settings
from fastapi import HTTPException

logger = logging.getLogger(__name__)

class NAMASTEService:
    def __init__(self):
        self.base_url = settings.NAMASTE_BASE_URL # Potentially for a local data source
        self.api_key = settings.NAMASTE_API_KEY # Keep for consistency, though not used for public API

    async def search_namaste(self, query: str, ayush_system: Optional[str] = None) -> List[NAMASTETerm]:
        """Search NAMASTE database for AYUSH terms using local data"""
        logger.info(f"Searching NAMASTE for query: '{query}' with system: '{ayush_system}'")
        try:
            # Simulate fetching data from a local JSON file
            with open('data/namaste_data.json', 'r', encoding='utf-8') as f:
                data = json.load(f)

            results = []
            for item in data.get("results", []):
                # Basic filtering: match query against term and optionally system
                if query.lower() in item.get("term", "").lower():
                    if ayush_system is None or item.get("system", "").lower() == ayush_system.lower():
                        results.append(NAMASTETerm(
                            id=item.get("id", ""),
                            term=item.get("term", ""),
                            term_hindi=item.get("term_hindi"),
                            category=item.get("category", ""),
                            subcategory=item.get("subcategory"),
                            ayush_system=item.get("system", ""),
                            description=item.get("description"),
                            synonyms=item.get("synonyms", [])
                        ))
            logger.info(f"Found {len(results)} NAMASTE matches for query: '{query}'")
            return results
        except FileNotFoundError:
            logger.error("NAMASTE data file not found: 'data/namaste_data.json'")
            # Return mock data for demonstration if file is missing
            return [
                NAMASTETerm(
                    id="NAM001",
                    term=query,
                    term_hindi="अनुवाद",
                    category="Disease",
                    subcategory="Fever",
                    ayush_system="Ayurveda",
                    description="Traditional Ayurvedic terminology for a symptom.",
                    synonyms=["variant1", "variant2"]
                )
            ]
        except Exception as e:
            logger.error(f"Error searching NAMASTE database: {e}")
            # Return mock data on error
            return [
                NAMASTETerm(
                    id="NAM001",
                    term=query,
                    term_hindi="अनुवाद",
                    category="Disease",
                    subcategory="Fever",
                    ayush_system="Ayurveda",
                    description="Traditional Ayurvedic terminology for a symptom.",
                    synonyms=["variant1", "variant2"]
                )
            ]
