from backend.app.services.ollama_extraction_service import (
    extract_structured_opportunity,
)

raw_text = """
Nous recherchons un Consultant IA senior pour accompagner des projets
de transformation data et intelligence artificielle dans le secteur santé / biotech.
Missions : cadrage de cas d’usage GenAI, prototypage avec Python,
accompagnement métier, ateliers clients, vulgarisation technique.
Profil : 3 à 5 ans d’expérience, bonne maîtrise du machine learning,
LLM, API, data science.
Poste hybride basé à Paris, 2 jours de télétravail.
CDI.
Salaire entre 55000 et 70000 euros.
"""

result = extract_structured_opportunity(raw_text)

print(result.model_dump())
