from fastapi import APIRouter, Query, HTTPException
from typing import List, Optional

from app.api.models.common import SearchType, NAMASTETerm, ICD11Term
from app.api.services.mapping import MappingService

router = APIRouter()

# Initialize services (singleton pattern implicitly via import)
mapping_service = MappingService()

@router.get("/api/v1/search")
async def search_terms(
    q: str = Query(..., description="Search query"),
    source: SearchType = Query(SearchType.BOTH, description="Search source (namaste, icd11, or both)"),
    ayush_system: Optional[str] = Query(None, description="Filter by AYUSH system (e.g., Ayurveda, Yoga)")
):
    """Search for terms in NAMASTE and/or ICD-11"""
    results: Dict[str, Any] = {
        "query": q,
        "source": source.value,
        "namaste_results": [],
        "icd11_results": []
    }

    if source in [SearchType.NAMASTE, SearchType.BOTH]:
        namaste_results = await mapping_service.namaste_service.search_namaste(q, ayush_system)
        results["namaste_results"] = namaste_results

    if source in [SearchType.ICD11, SearchType.BOTH]:
        icd11_results = await mapping_service.icd11_service.search_icd11(q)
        results["icd11_results"] = icd11_results

    return results