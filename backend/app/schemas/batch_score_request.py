from pydantic import BaseModel, Field

from backend.app.schemas.score_request import ScoreRequest


class BatchScoreRequest(BaseModel):
    opportunities: list[ScoreRequest] = Field(default_factory=list)
