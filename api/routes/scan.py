from fastapi import APIRouter, BackgroundTasks

from pydantic import BaseModel

from scanner import Scanner
from utils.progress import ScanProgress


router = APIRouter(
    prefix="/api",
    tags=["Scanner"]
)


class ScanRequest(BaseModel):
    websites: list[str]


@router.post("/scan")
def scan(
    request: ScanRequest,
    background_tasks: BackgroundTasks
):

    ScanProgress.reset(
        len(request.websites)
    )

    background_tasks.add_task(
        Scanner.run_websites,
        request.websites
    )

    return {
        "success": True,
        "message": "Scan started.",
        "total": len(request.websites)
    }


@router.get("/scan/status")
def scan_status():

    return ScanProgress.data()