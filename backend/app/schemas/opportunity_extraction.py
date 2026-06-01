from pydantic import BaseModel, Field, field_validator


class OpportunityExtraction(BaseModel):
    title: str | None = None
    company: str | None = None
    location: str | None = None

    remote_type: str | None = None
    contract_type: str | None = None
    seniority_level: str | None = None

    salary_min: float | None = None
    salary_max: float | None = None

    domains: list[str] = Field(default_factory=list)
    skills: list[str] = Field(default_factory=list)
    tools: list[str] = Field(default_factory=list)

    summary: str | None = None
    key_missions: list[str] = Field(default_factory=list)
    candidate_profile: list[str] = Field(default_factory=list)

    @field_validator(
        "domains",
        "skills",
        "tools",
        "key_missions",
        "candidate_profile",
        mode="before",
    )
    @classmethod
    def none_to_empty_list(cls, value):
        if value is None:
            return []

        return value
