from pydantic import BaseModel


class UserProfile(BaseModel):
    target_roles: list[str]

    preferred_domains: list[str]

    preferred_skills: list[str]

    preferred_locations: list[str]

    salary_expectation: float

    remote_preference: str

    seniority_target: str
