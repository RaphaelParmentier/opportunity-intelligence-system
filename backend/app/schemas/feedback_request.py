from pydantic import BaseModel


class FeedbackRequest(BaseModel):
    opportunity_title: str
    source_url: str | None = None
    overall_score: float | None = None

    action: str
    comment: str | None = None
