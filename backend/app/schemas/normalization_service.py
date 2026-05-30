from backend.app.core.taxonomies import (
    TARGET_ROLE_ALIASES,
    DOMAIN_ALIASES,
    REMOTE_TYPE_ALIASES,
    SENIORITY_ALIASES,
    CONTRACT_TYPE_ALIASES,
)


def normalize_text(value: str | None) -> str:
    if not value:
        return ""

    return value.lower().strip()


def match_alias(value: str | None, alias_mapping: dict[str, list[str]]) -> str | None:
    normalized_value = normalize_text(value)

    if not normalized_value:
        return None

    for canonical_value, aliases in alias_mapping.items():
        for alias in aliases:
            if alias in normalized_value:
                return canonical_value

    return None


def normalize_role(value: str | None) -> str | None:
    return match_alias(value, TARGET_ROLE_ALIASES)


def normalize_domain(value: str | None) -> str | None:
    return match_alias(value, DOMAIN_ALIASES)


def normalize_remote_type(value: str | None) -> str | None:
    return match_alias(value, REMOTE_TYPE_ALIASES)


def normalize_seniority(value: str | None) -> str | None:
    return match_alias(value, SENIORITY_ALIASES)


def normalize_contract_type(value: str | None) -> str | None:
    return match_alias(value, CONTRACT_TYPE_ALIASES)


def normalize_many(values: list[str], alias_mapping: dict[str, list[str]]) -> list[str]:
    normalized_values = []

    for value in values:
        normalized = match_alias(value, alias_mapping)

        if normalized and normalized not in normalized_values:
            normalized_values.append(normalized)

    return normalized_values
