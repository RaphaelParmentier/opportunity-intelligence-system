from datetime import datetime

from pydantic import BaseModel, Field


class UserFeedback(BaseModel):
    opportunity_id: str

    action: str

    comment: str | None = None

    created_at: datetime = Field(default_factory=datetime.utcnow)
