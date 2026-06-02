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


def get_feedback_stats() -> dict:
    feedback_entries = load_feedback()

    stats = {
        "total": len(feedback_entries),
        "actions": {},
        "average_score_by_action": {},
    }

    for entry in feedback_entries:
        action = entry["action"]
        score = entry.get("overall_score")

        stats["actions"][action] = stats["actions"].get(action, 0) + 1

        if score is not None:
            if action not in stats["average_score_by_action"]:
                stats["average_score_by_action"][action] = {
                    "sum": 0,
                    "count": 0,
                }

            stats["average_score_by_action"][action]["sum"] += score
            stats["average_score_by_action"][action]["count"] += 1

    for action, values in stats["average_score_by_action"].items():
        stats["average_score_by_action"][action] = round(
            values["sum"] / values["count"],
            2,
        )

    return stats
