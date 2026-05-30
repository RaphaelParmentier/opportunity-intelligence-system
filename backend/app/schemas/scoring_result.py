from pydantic import BaseModel


class ScoringResult(BaseModel):
    opportunity_id: str

    overall_score: float

    ai_score: float

    data_score: float

    healthcare_score: float

    teaching_score: float

    consulting_score: float

    remote_score: float

    salary_score: float

    strategic_score: float

    explanation: str
