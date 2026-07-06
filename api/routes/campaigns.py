from fastapi import APIRouter

from database.campaign_repository import CampaignRepository


router = APIRouter(
    prefix="/api",
    tags=["Campaigns"]
)

repo = CampaignRepository()


@router.get("/campaigns")
def campaigns():

    campaigns = repo.all()

    return {
        "total": len(campaigns),
        "campaigns": campaigns
    }