from fastapi import FastAPI

from backend.app.schemas.score_request import ScoreRequest
from backend.app.services.ollama_extraction_service import (
    extract_opportunity_with_ollama,
)
from backend.app.services.rule_based_scoring_service import score_opportunity
from backend.app.test_pipeline import build_default_user_profile

app = FastAPI(
    title="Opportunity Intelligence System API",
    version="0.1.0",
)


@app.get("/")
def healthcheck():
    return {
        "status": "ok",
        "service": "opportunity-intelligence-system",
        "version": "0.1.0",
    }


@app.post("/score")
def score_raw_opportunity(request: ScoreRequest):
    user_profile = build_default_user_profile()

    opportunity = extract_opportunity_with_ollama(
        source=request.source,
        source_url=request.source_url,
        raw_text=request.raw_text,
    )

    scoring = score_opportunity(
        opportunity=opportunity,
        user_profile=user_profile,
    )

    return {
        "opportunity": opportunity.model_dump(),
        "scoring": scoring.model_dump(),
    }
