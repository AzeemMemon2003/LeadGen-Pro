from fastapi import APIRouter
from pydantic import BaseModel

from database.repository import LeadRepository

router = APIRouter()


class StatusUpdate(BaseModel):
    status: str


@router.get("/leads")
def get_leads():

    repo = LeadRepository()

    leads = repo.all()

    repo.db.close()

    return leads


@router.put("/leads/{lead_id}")
def update_lead_status(lead_id: int, payload: StatusUpdate):

    repo = LeadRepository()

    repo.update_status(lead_id, payload.status)

    repo.db.close()

    return {
        "success": True,
        "message": "Lead updated successfully."
    }