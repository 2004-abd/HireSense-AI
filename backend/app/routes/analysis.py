from datetime import datetime, timezone
from fastapi import APIRouter, Depends, File, Form, UploadFile
from app.database import analyses_collection, logs_collection
from app.ml.file_parser import extract_text_from_upload
from app.ml.model import analyze_resume_fit
from app.schemas import ResumeAnalysisRequest, ResumeAnalysisResponse
from app.security import get_current_user

router = APIRouter(prefix="/analysis", tags=["Resume Analysis"])

async def save_analysis(current_user: dict, resume_text: str, job_description: str, result: dict, source: str):
    doc = {"user_email": current_user["email"], "source": source, "resume_preview": resume_text[:350], "job_preview": job_description[:350], "result": result, "created_at": datetime.now(timezone.utc)}
    await analyses_collection.insert_one(doc)
    await logs_collection.insert_one({"user_email": current_user["email"], "action": "resume_fit_analysis", "source": source, "created_at": datetime.now(timezone.utc)})

@router.post("/resume-fit", response_model=ResumeAnalysisResponse)
async def resume_fit(payload: ResumeAnalysisRequest, current_user: dict = Depends(get_current_user)):
    result = analyze_resume_fit(payload.resume_text, payload.job_description)
    await save_analysis(current_user, payload.resume_text, payload.job_description, result, "text")
    return result

@router.post("/resume-fit-file", response_model=ResumeAnalysisResponse)
async def resume_fit_file(resume_file: UploadFile = File(...), job_description: str = Form(...), current_user: dict = Depends(get_current_user)):
    resume_text = await extract_text_from_upload(resume_file)
    result = analyze_resume_fit(resume_text, job_description)
    await save_analysis(current_user, resume_text, job_description, result, "file")
    return result

@router.get("/history")
async def get_history(current_user: dict = Depends(get_current_user)):
    cursor = analyses_collection.find({"user_email": current_user["email"]}, {"_id": 0}).sort("created_at", -1).limit(20)
    history = []
    async for item in cursor:
        item["created_at"] = item["created_at"].isoformat()
        history.append(item)
    return history
