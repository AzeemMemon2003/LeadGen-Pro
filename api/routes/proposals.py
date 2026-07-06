from fastapi import APIRouter

from proposal.proposal_repository import ProposalRepository


router = APIRouter(
    prefix="/api",
    tags=["Proposals"]
)

repo = ProposalRepository()


@router.get("/proposals")
def proposals():

    return {
        "total": repo.count(),
        "proposals": repo.all()
    }