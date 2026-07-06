from fastapi import FastAPI

from api.routes.leads import router as leads_router
from api.routes.scan import router as scan_router
from fastapi.middleware.cors import CORSMiddleware
from api.routes.dashboard import router as dashboard_router

app = FastAPI(
    title="LeadGen Pro API",
    description="Lead Intelligence Platform",
    version="5.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "name": "LeadGen Pro",
        "version": "5.0.0",
        "status": "running"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

app.include_router(
    leads_router,
    prefix="/api",
    tags=["Leads"]
)

app.include_router(
    scan_router,
    tags=["Scanner"]
)
app.include_router(
    dashboard_router,
    prefix="/api",
    tags=["Dashboard"]
)