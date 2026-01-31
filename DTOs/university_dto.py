from pydantic import BaseModel
from typing import List, Optional

class University(BaseModel):
    name: str
    website: Optional[str]

class UniversitiesResponse(BaseModel):
    country: str
    total: int
    universities: List[University]
