from fastapi import APIRouter

from database.scan_history_repository import ScanHistoryRepository


router = APIRouter(
    prefix="/api",
    tags=["History"]
)

repo = ScanHistoryRepository()


@router.get("/history")
def history():

    return {

        "history": repo.all()

    }