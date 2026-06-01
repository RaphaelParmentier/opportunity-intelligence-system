import json

import requests

from backend.app.schemas.opportunity import Opportunity
from backend.app.schemas.opportunity_extraction import OpportunityExtraction
from backend.app.services.extraction_enrichment_service import (
    enrich_domains_with_taxonomies,
)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5:7b"


def build_extraction_prompt(raw_text: str) -> str:
    return f"""
You are an information extraction system for job opportunities.

Extract structured information from the following job description.

Return only valid JSON. No markdown. No explanation.
If information is missing, use null.
Never invent information.

Use English canonical labels when possible.

Domain classification rules:
- If the text mentions IA, AI, intelligence artificielle, generative AI, GenAI, LLM or machine learning, include "artificial_intelligence".
- If the text mentions data, data science, analytics, statistics, machine learning or modeling, include "data_science".
- If the text mentions santé, healthcare, pharma, biotech, clinical or life sciences, include "healthcare".
- If the text mentions formation, teaching, cours, pédagogie or training, include "education".
- If the text mentions conseil, consulting, accompagnement client, ateliers clients or transformation projects, include "consulting".
- If the text mentions API, backend, frontend, application, software, development or prototyping, include "software".
- A job can belong to several domains.

Expected JSON schema:
{{
  "title": "string",
  "company": "string or null",
  "location": "string or null",
  "remote_type": "remote | hybrid | onsite | null",
  "contract_type": "permanent | fixed_term | freelance | internship | apprenticeship | null",
  "salary_min": number or null,
  "salary_max": number or null,
  "seniority_level": "junior | mid | senior | null",
  "domains": ["artificial_intelligence", "data_science", "healthcare", "education", "consulting", "software"],
  "skills": ["python", "machine_learning", "llm", "statistics"],
  "tools": ["fastapi", "postgresql", "docker"],
  "summary": "short summary in English",
  "key_missions": ["mission 1", "mission 2"],
  "candidate_profile": ["requirement 1", "requirement 2"]
}}

Job description:
{raw_text}
"""


def extract_structured_opportunity(raw_text: str) -> OpportunityExtraction:
    prompt = build_extraction_prompt(raw_text)
    extracted = call_ollama(prompt)

    extraction = OpportunityExtraction(**extracted)
    extraction = enrich_domains_with_taxonomies(raw_text, extraction)

    return extraction


def call_ollama(prompt: str) -> dict:
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False,
            "format": "json",
        },
        timeout=60,
    )

    response.raise_for_status()

    payload = response.json()
    raw_response = payload["response"]

    return json.loads(raw_response)


def extract_opportunity_with_ollama(
    source: str,
    source_url: str | None,
    raw_text: str,
) -> Opportunity:
    extracted = extract_structured_opportunity(raw_text)

    return Opportunity(
        source=source,
        source_url=source_url,
        title=extracted.title or "Unknown title",
        company=extracted.company or "Unknown company",
        location=extracted.location,
        remote_type=extracted.remote_type,
        contract_type=extracted.contract_type,
        salary_min=extracted.salary_min,
        salary_max=extracted.salary_max,
        seniority_level=extracted.seniority_level,
        description=raw_text,
    )

    return Opportunity(
        source=source,
        source_url=source_url,
        title=extracted.get("title") or "Unknown title",
        company=extracted.get("company") or "Unknown company",
        location=extracted.get("location"),
        remote_type=extracted.get("remote_type"),
        contract_type=extracted.get("contract_type"),
        salary_min=extracted.get("salary_min"),
        salary_max=extracted.get("salary_max"),
        seniority_level=extracted.get("seniority_level"),
        description=raw_text,
    )
