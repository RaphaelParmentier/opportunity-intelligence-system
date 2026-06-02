from pydantic import BaseModel

from backend.app.schemas.user_profile_request import UserProfileRequest


class ScoreOpportunityRequest(BaseModel):
    source: str = "manual"

    source_url: str | None = None

    raw_text: str

    profile: UserProfileRequest
