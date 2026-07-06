from fastapi import APIRouter

from database.repository import LeadRepository

router = APIRouter()


@router.get("/dashboard")
def dashboard():

    repo = LeadRepository()

    leads = repo.all()

    total = len(leads)

    high = 0
    medium = 0
    low = 0

    contacted = 0
    verified = 0

    total_score = 0

    proposals = 0

    for lead in leads:

        priority = (lead.get("priority") or "").upper()

        if priority == "HIGH":
            high += 1
        elif priority == "MEDIUM":
            medium += 1
        else:
            low += 1

        if (lead.get("status") or "").lower() == "contacted":
            contacted += 1

        if lead.get("email_verified"):
            verified += 1

        total_score += lead.get("score", 0)

        if lead.get("proposal"):
            proposals += 1

    average_score = (
        round(total_score / total, 1)
        if total
        else 0
    )

    success_rate = (
        round((verified / total) * 100, 1)
        if total
        else 0
    )

    return {

        "total_leads": total,

        "qualified": high + medium,

        "contacted": contacted,

        "high_priority": high,

        "verified_emails": verified,

        "average_score": average_score,

        "proposal_count": proposals,

        "success_rate": success_rate,

        "priority_distribution": {

            "high": high,

            "medium": medium,

            "low": low,

        },

        "recent_activity": leads[:5],

    }