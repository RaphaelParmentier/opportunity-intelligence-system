from backend.app.schemas.user_profile import UserProfile


def build_default_raphael_profile() -> UserProfile:
    return UserProfile(
        target_roles=[
            "ai_consultant",
            "ai_engineer",
            "ml_engineer",
            "data_scientist",
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
            "software",
        ],
        preferred_skills=[
            "python",
            "machine_learning",
            "llm",
            "statistics",
            "data_science",
            "fastapi",
            "bioinformatics",
            "biostatistics",
            "teaching",
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
