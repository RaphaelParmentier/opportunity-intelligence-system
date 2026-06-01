from backend.app.core.taxonomies import DOMAIN_ALIASES
from backend.app.schemas.opportunity import Opportunity
from backend.app.schemas.scoring_result import ScoringResult
from backend.app.schemas.user_profile import UserProfile
from backend.app.services.normalization_service import (
    normalize_contract_type,
    normalize_many,
    normalize_remote_type,
    normalize_role,
    normalize_seniority,
)


def score_domain(opportunity: Opportunity, domain: str) -> float:
    return 100.0 if domain in opportunity.domains else 0.0


def score_presence(text: str, aliases: list[str], high_score: float = 100.0) -> float:
    normalized_text = text.lower()

    for alias in aliases:
        if alias.lower() in normalized_text:
            return high_score

    return 0.0


def score_salary(opportunity: Opportunity, user_profile: UserProfile) -> float:
    if opportunity.salary_min is None and opportunity.salary_max is None:
        return 50.0

    salary_reference = opportunity.salary_max or opportunity.salary_min

    if salary_reference is None:
        return 50.0

    ratio = salary_reference / user_profile.salary_expectation

    if ratio >= 1.1:
        return 100.0

    if ratio >= 1.0:
        return 90.0

    if ratio >= 0.9:
        return 75.0

    if ratio >= 0.8:
        return 60.0

    return 35.0


def score_remote(opportunity: Opportunity, user_profile: UserProfile) -> float:
    normalized_remote = normalize_remote_type(opportunity.remote_type)

    if normalized_remote == user_profile.remote_preference:
        return 100.0

    if normalized_remote == "hybrid" and user_profile.remote_preference == "remote":
        return 80.0

    if normalized_remote == "remote" and user_profile.remote_preference == "hybrid":
        return 95.0

    if normalized_remote == "onsite":
        return 25.0

    return 50.0


def score_opportunity(
    opportunity: Opportunity, user_profile: UserProfile
) -> ScoringResult:
    text = f"{opportunity.title} {opportunity.description}".lower()

    normalized_role = normalize_role(opportunity.title)
    normalized_domains = normalize_many(
        [opportunity.description],
        DOMAIN_ALIASES,
    )
    normalized_seniority = normalize_seniority(opportunity.seniority_level)
    normalized_contract = normalize_contract_type(opportunity.contract_type)

    ai_score = score_domain(
        opportunity,
        "artificial_intelligence",
    )

    data_score = score_domain(
        opportunity,
        "data_science",
    )

    healthcare_score = score_domain(
        opportunity,
        "healthcare",
    )

    teaching_score = score_domain(
        opportunity,
        "education",
    )

    consulting_score = score_domain(
        opportunity,
        "consulting",
    )

    remote_score = score_remote(opportunity, user_profile)
    salary_score = score_salary(opportunity, user_profile)

    role_score = 100.0 if normalized_role in user_profile.target_roles else 50.0
    seniority_score = (
        90.0 if normalized_seniority == user_profile.seniority_target else 65.0
    )

    strategic_score = (
        0.35 * role_score
        + 0.25 * ai_score
        + 0.15 * data_score
        + 0.15 * healthcare_score
        + 0.10 * seniority_score
    )

    overall_score = (
        0.25 * strategic_score
        + 0.20 * ai_score
        + 0.15 * data_score
        + 0.15 * remote_score
        + 0.15 * salary_score
        + 0.10 * consulting_score
    )

    explanation = (
        f"Normalized role={normalized_role}, "
        f"domains={opportunity.domains}, "
        f"seniority={normalized_seniority}, "
        f"contract={normalized_contract}."
    )

    return ScoringResult(
        opportunity_id=opportunity.id or "temporary",
        overall_score=round(overall_score, 2),
        ai_score=ai_score,
        data_score=data_score,
        healthcare_score=healthcare_score,
        teaching_score=teaching_score,
        consulting_score=consulting_score,
        remote_score=remote_score,
        salary_score=salary_score,
        strategic_score=round(strategic_score, 2),
        explanation=explanation,
    )
