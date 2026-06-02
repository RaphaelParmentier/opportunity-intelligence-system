from backend.app.schemas.user_profile import UserProfile
from backend.app.schemas.user_profile_request import (
    UserProfileRequest,
)


def build_user_profile(
    request: UserProfileRequest,
) -> UserProfile:
    return UserProfile(
        target_roles=request.target_roles,
        preferred_domains=request.preferred_domains,
        preferred_skills=request.preferred_skills,
        preferred_locations=request.preferred_locations,
        salary_expectation=request.salary_expectation,
        remote_preference=request.remote_preference,
        seniority_target=request.seniority_target,
    )
