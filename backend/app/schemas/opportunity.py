from datetime import datetime
from typing import Optional

from pydantic import BaseModel


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

    from pydantic import Field

    domains: list[str] = Field(default_factory=list)
    skills: list[str] = Field(default_factory=list)
    tools: list[str] = Field(default_factory=list)

    key_missions: list[str] = Field(default_factory=list)
    candidate_profile: list[str] = Field(default_factory=list)

    summary: str | None = None

    description: str

    created_at: datetime = Field(default_factory=datetime.utcnow)
