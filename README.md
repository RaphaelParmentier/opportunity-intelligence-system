# Opportunity Intelligence System

## Vision

Construire un copilote de carrière intelligent combinant Intelligence Artificielle, Machine Learning et systèmes de recommandation.

L'objectif n'est pas simplement de rechercher des offres d'emploi mais d'aider l'utilisateur à identifier, comprendre, prioriser et suivre les opportunités les plus pertinentes pour son profil.

---

## Problématique

La recherche d'emploi moderne implique :

- plusieurs plateformes
- plusieurs formats d'offres
- beaucoup de bruit
- peu de personnalisation

Les moteurs de recherche actuels filtrent mais n'apprennent pas réellement les préférences de l'utilisateur.

Opportunity Intelligence System vise à créer un moteur de recommandation personnalisé capable d'apprendre progressivement les préférences réelles de son utilisateur.

---

## Vision Long Terme

Le système devra :

1. Collecter les opportunités depuis différentes sources.
2. Extraire les informations pertinentes à l'aide d'un LLM.
3. Normaliser les informations dans un format commun.
4. Scorer les opportunités selon des critères explicables.
5. Apprendre des actions de l'utilisateur.
6. Prédire les opportunités les plus pertinentes.
7. Agir comme un véritable copilote de carrière.

---

## Architecture Cible

Sources
↓
Ingestion Layer
↓
LLM Extraction
↓
Normalization Layer
↓
Scoring Engine
↓
Feedback Collection
↓
Machine Learning Ranking
↓
Career Copilot Interface

---

## Technologies Prévisionnelles

Frontend

- Next.js

Backend

- FastAPI

Machine Learning

- scikit-learn
- XGBoost

LLM

- Ollama

Embeddings

- sentence-transformers

Database

- PostgreSQL

Vector Search

- pgvector (V2)

Deployment

- Docker

---

## Principes de Conception

- LLM agnostique
- Multilingue français / anglais
- Architecture modulaire
- Explicabilité des scores
- Machine Learning basé sur le feedback utilisateur
- Déploiement local possible

---

## MVP V1

Import manuel :

- CSV
- Copier-coller d'offres

Pipeline :

Offre
↓
Extraction
↓
Normalisation
↓
Scoring
↓
Dashboard

---

## Évolutions Futures

V2

- APIs externes
- Connecteurs APEC
- Connecteurs France Travail

V3

- Veille automatique

V4

- Agent carrière autonome

---

## Décisions Techniques Actuelles

- Pas de LangChain dans le MVP.
- Ollama local pour limiter les coûts.
- FastAPI pour l'API.
- Scoring explicable avant Machine Learning.
- Machine Learning basé sur le feedback utilisateur.
- Support natif français et anglais.
