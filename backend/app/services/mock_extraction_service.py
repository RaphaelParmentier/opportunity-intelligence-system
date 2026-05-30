import re

from backend.app.schemas.opportunity import Opportunity


def extract_salary(raw_text: str) -> tuple[float | None, float | None]:
    numbers = re.findall(r"\b\d{5,6}\b", raw_text.replace(" ", ""))

    if len(numbers) >= 2:
        return float(numbers[0]), float(numbers[1])

    if len(numbers) == 1:
        return float(numbers[0]), None

    return None, None


def mock_extract_opportunity(
    source: str, source_url: str | None, raw_text: str
) -> Opportunity:
    lower_text = raw_text.lower()

    if "consultant ia" in lower_text:
        title = "Consultant IA senior"
        company = "HealthTech AI"
    elif "data analyst" in lower_text:
        title = "Junior Data Analyst"
        company = "Retail Company"
    elif "formateur ia" in lower_text:
        title = "Formateur IA & Data Science"
        company = "Organisme de formation"
    else:
        title = "Unknown opportunity"
        company = "Unknown company"

    salary_min, salary_max = extract_salary(raw_text)

    return Opportunity(
        source=source,
        source_url=source_url,
        title=title,
        company=company,
        location="Paris" if "paris" in lower_text else None,
        remote_type=raw_text,
        contract_type=raw_text,
        salary_min=salary_min,
        salary_max=salary_max,
        seniority_level=raw_text,
        description=raw_text,
    )
