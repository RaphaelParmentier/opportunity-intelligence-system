from pydantic import BaseModel


class OpportunityExtraction(BaseModel):
    title: str | None = None
    company: str | None = None
    location: str | None = None

    remote_type: str | None = None
    contract_type: str | None = None
    seniority_level: str | None = None

    salary_min: float | None = None
    salary_max: float | None = None

    domains: list[str] = []
    skills: list[str] = []
    tools: list[str] = []

    summary: str | None = None
    key_missions: list[str] = []
    candidate_profile: list[str] = []
