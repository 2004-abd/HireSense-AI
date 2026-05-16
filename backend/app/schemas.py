from typing import List
from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    name: str = Field(min_length=2, max_length=80)
    email: EmailStr
    password: str = Field(min_length=6, max_length=72)

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user_name: str
    email: EmailStr

class ResumeAnalysisRequest(BaseModel):
    resume_text: str = Field(min_length=50)
    job_description: str = Field(min_length=30)

class ResumeAnalysisResponse(BaseModel):
    fit_category: str
    fit_score: float
    confidence: float
    skill_match_rate: float
    matched_skills: List[str]
    missing_skills: List[str]
    suggestions: List[str]

class MetricsResponse(BaseModel):
    accuracy: float
    precision: float
    recall: float
    f1_score: float
    labels: List[str]
    confusion_matrix: List[List[int]]
