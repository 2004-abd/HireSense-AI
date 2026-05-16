from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import FRONTEND_ORIGIN
from app.ml.model import load_model
from app.routes import auth, analysis, metrics

app = FastAPI(
    title="HireSense AI API",
    description="AI Resume & Job Fit Analyzer with JWT security and MongoDB logging.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_ORIGIN, "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_event():
    load_model()


@app.get("/")
def root():
    return {
        "project": "HireSense AI",
        "status": "running",
        "docs": "/docs",
    }


app.include_router(auth.router)
app.include_router(analysis.router)
app.include_router(metrics.router)
