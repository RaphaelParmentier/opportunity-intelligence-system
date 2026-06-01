from backend.app.core.taxonomies import DOMAIN_ALIASES
from backend.app.schemas.opportunity_extraction import OpportunityExtraction
from backend.app.services.normalization_service import normalize_many


def build_text_for_enrichment(
    raw_text: str,
    extraction: OpportunityExtraction,
) -> str:
    parts = [
        raw_text,
        extraction.title or "",
        extraction.summary or "",
        " ".join(extraction.domains),
        " ".join(extraction.skills),
        " ".join(extraction.tools),
        " ".join(extraction.key_missions),
        " ".join(extraction.candidate_profile),
    ]

    return " ".join(parts)


def enrich_domains_with_taxonomies(
    raw_text: str,
    extraction: OpportunityExtraction,
) -> OpportunityExtraction:
    enrichment_text = build_text_for_enrichment(raw_text, extraction)

    taxonomy_domains = normalize_many(
        [enrichment_text],
        DOMAIN_ALIASES,
    )

    merged_domains = list(extraction.domains)

    for domain in taxonomy_domains:
        if domain not in merged_domains:
            merged_domains.append(domain)

    extraction.domains = merged_domains

    return extraction
