import json
from pathlib import Path

from backend.app.schemas.user_profile import UserProfile
from backend.app.services.mock_extraction_service import mock_extract_opportunity
from backend.app.services.rule_based_scoring_service import score_opportunity


def load_sample_opportunities() -> list[dict]:
    path = Path("data/examples/sample_opportunities.json")

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def build_default_user_profile() -> UserProfile:
    return UserProfile(
        target_roles=[
            "ai_engineer",
            "ml_engineer",
            "data_scientist",
            "ai_consultant",
            "data_consultant",
            "data_product_manager",
            "ai_trainer",
        ],
        preferred_domains=[
            "artificial_intelligence",
            "data_science",
            "healthcare",
            "education",
            "consulting",
        ],
        preferred_skills=[
            "python",
            "machine learning",
            "llm",
            "fastapi",
            "data science",
            "statistics",
        ],
        preferred_locations=[
            "Paris",
            "Fontainebleau",
            "remote",
            "hybrid",
        ],
        salary_expectation=55000,
        remote_preference="hybrid",
        seniority_target="senior",
    )


def main() -> None:
    samples = load_sample_opportunities()
    user_profile = build_default_user_profile()

    for sample in samples:
        opportunity = mock_extract_opportunity(
            source=sample["source"],
            source_url=sample.get("source_url"),
            raw_text=sample["raw_text"],
        )

        scoring = score_opportunity(opportunity, user_profile)

        print("=" * 80)
        print(f"Title: {opportunity.title}")
        print(f"Company: {opportunity.company}")
        print(f"Salary: {opportunity.salary_min} - {opportunity.salary_max}")
        print("-" * 80)
        print(f"Overall score: {scoring.overall_score}")
        print(f"Strategic score: {scoring.strategic_score}")
        print(f"AI score: {scoring.ai_score}")
        print(f"Data score: {scoring.data_score}")
        print(f"Healthcare score: {scoring.healthcare_score}")
        print(f"Teaching score: {scoring.teaching_score}")
        print(f"Consulting score: {scoring.consulting_score}")
        print(f"Remote score: {scoring.remote_score}")
        print(f"Salary score: {scoring.salary_score}")
        print(f"Explanation: {scoring.explanation}")


if __name__ == "__main__":
    main()
