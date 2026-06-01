from pydantic import BaseModel


class ScoreRequest(BaseModel):
    source: str = "manual"
    source_url: str | None = None
    raw_text: str
