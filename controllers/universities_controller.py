from fastapi import APIRouter, HTTPException
from services.universities_service import get_universities_by_country

router = APIRouter(
    prefix="/universities",
    tags=["Universities"]
)


@router.get("/{country}")
def universities_by_country(country: str):
    try:
        return get_universities_by_country(country)
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Error consultando la API de universidades"
        )
