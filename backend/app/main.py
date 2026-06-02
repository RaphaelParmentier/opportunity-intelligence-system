from fastapi import FastAPI

from backend.app.schemas.batch_score_request import BatchScoreRequest
from backend.app.schemas.feedback_request import FeedbackRequest
from backend.app.schemas.score_opportunity_request import (
    ScoreOpportunityRequest,
)
from backend.app.schemas.score_request import ScoreRequest
from backend.app.services.default_profile_service import (
    build_default_raphael_profile,
)
from backend.app.services.feedback_service import (
    get_feedback_stats,
    load_feedback,
    save_feedback_entry,
)
from backend.app.services.ollama_extraction_service import (
    extract_opportunity_with_ollama,
)
from backend.app.services.rule_based_scoring_service import score_opportunity
from backend.app.services.user_profile_service import (
    build_user_profile,
)

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


@app.post("/extract")
def extract_raw_opportunity(request: ScoreRequest):
    opportunity = extract_opportunity_with_ollama(
        source=request.source,
        source_url=request.source_url,
        raw_text=request.raw_text,
    )

    return {
        "opportunity": opportunity.model_dump(),
    }


@app.post("/score/default")
def score_raw_opportunity_with_default_profile(request: ScoreRequest):
    user_profile = build_default_raphael_profile()

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
        "profile": user_profile.model_dump(),
        "opportunity": opportunity.model_dump(),
        "scoring": scoring.model_dump(),
    }


@app.post("/score")
def score_raw_opportunity(
    request: ScoreOpportunityRequest,
):
    user_profile = build_user_profile(
        request.profile,
    )

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


@app.post("/score/batch/default")
def score_batch_with_default_profile(request: BatchScoreRequest):
    user_profile = build_default_raphael_profile()

    results = []

    for item in request.opportunities:
        opportunity = extract_opportunity_with_ollama(
            source=item.source,
            source_url=item.source_url,
            raw_text=item.raw_text,
        )

        scoring = score_opportunity(
            opportunity=opportunity,
            user_profile=user_profile,
        )

        results.append(
            {
                "opportunity": opportunity.model_dump(),
                "scoring": scoring.model_dump(),
            }
        )

    results = sorted(
        results,
        key=lambda result: result["scoring"]["overall_score"],
        reverse=True,
    )

    return {
        "count": len(results),
        "results": results,
    }


@app.post("/feedback")
def create_feedback(request: FeedbackRequest):
    entry = save_feedback_entry(request)

    return {
        "status": "saved",
        "feedback": entry,
    }


@app.get("/feedback")
def list_feedback():
    return {
        "count": len(load_feedback()),
        "feedback": load_feedback(),
    }


@app.get("/feedback/stats")
def feedback_stats():
    return get_feedback_stats()
