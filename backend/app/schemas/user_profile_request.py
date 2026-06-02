from pydantic import BaseModel, Field


class UserProfileRequest(BaseModel):
    target_roles: list[str] = Field(default_factory=list)

    preferred_domains: list[str] = Field(default_factory=list)

    preferred_skills: list[str] = Field(default_factory=list)

    preferred_locations: list[str] = Field(default_factory=list)

    salary_expectation: float = 0

    remote_preference: str | None = None

    seniority_target: str | None = None
