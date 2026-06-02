import json
from datetime import datetime
from pathlib import Path

from backend.app.schemas.feedback_request import FeedbackRequest

FEEDBACK_PATH = Path("storage/feedback.json")


def load_feedback() -> list[dict]:
    if not FEEDBACK_PATH.exists():
        return []

    with FEEDBACK_PATH.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_feedback_entry(request: FeedbackRequest) -> dict:
    feedback_entries = load_feedback()

    entry = {
        "opportunity_title": request.opportunity_title,
        "source_url": request.source_url,
        "overall_score": request.overall_score,
        "action": request.action,
        "comment": request.comment,
        "created_at": datetime.utcnow().isoformat(),
    }

    feedback_entries.append(entry)

    with FEEDBACK_PATH.open("w", encoding="utf-8") as file:
        json.dump(feedback_entries, file, ensure_ascii=False, indent=2)

    return entry
