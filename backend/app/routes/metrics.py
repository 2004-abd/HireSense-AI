import json
from datetime import datetime, timezone
from pathlib import Path
from fastapi import APIRouter, Depends, HTTPException
from app.database import metrics_collection
from app.schemas import MetricsResponse
from app.security import get_current_user

router = APIRouter(prefix="/metrics", tags=["Model Metrics"])
BASE_DIR = Path(__file__).resolve().parents[2]
METRICS_PATH = BASE_DIR / "app" / "ml" / "metrics.json"

@router.get("/model", response_model=MetricsResponse)
async def get_model_metrics(current_user: dict = Depends(get_current_user)):
    if not METRICS_PATH.exists():
        raise HTTPException(status_code=404, detail="Metrics not found. Train the model first.")
    metrics = json.loads(METRICS_PATH.read_text(encoding="utf-8"))
    await metrics_collection.update_one({"name":"resume_fit_model"}, {"$set": {"name":"resume_fit_model", "metrics": metrics, "updated_at": datetime.now(timezone.utc)}}, upsert=True)
    return metrics
