from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Opportunity(BaseModel):
    id: Optional[str] = None

    source: str
    source_url: Optional[str] = None

    title: str
    company: str

    location: Optional[str] = None

    remote_type: Optional[str] = None

    contract_type: Optional[str] = None

    salary_min: Optional[float] = None
    salary_max: Optional[float] = None

    seniority_level: Optional[str] = None

    description: str

    created_at: datetime = Field(default_factory=datetime.utcnow)
