from fastapi import APIRouter

from analytics.dashboard import Dashboard


router = APIRouter(
    prefix="/api",
    tags=["Analytics"]
)


@router.get("/analytics")
def analytics():

    dashboard = Dashboard()

    return dashboard.summary()