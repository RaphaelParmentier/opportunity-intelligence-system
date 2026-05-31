from backend.app.services.ollama_extraction_service import (
    extract_opportunity_with_ollama,
)

raw_text = """
Nous recherchons un Consultant IA senior pour accompagner des projets
de transformation data et intelligence artificielle dans le secteur santé.
Poste hybride basé à Paris.
CDI.
Salaire entre 55000 et 70000 euros.
"""

opportunity = extract_opportunity_with_ollama(
    source="manual",
    source_url=None,
    raw_text=raw_text,
)

print(opportunity.model_dump())
