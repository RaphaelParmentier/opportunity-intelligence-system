from pydantic import BaseModel


class OpportunityAnalysis(BaseModel):
    opportunity_id: str

    summary: str

    strengths: list[str]

    weaknesses: list[str]

    missing_skills: list[str]

    reasoning: str

    estimated_fit_score: float
