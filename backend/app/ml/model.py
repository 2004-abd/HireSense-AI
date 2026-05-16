from pathlib import Path
from typing import Any
import joblib
from sklearn.metrics.pairwise import cosine_similarity
from app.ml.skills import extract_skills, build_suggestions

BASE_DIR = Path(__file__).resolve().parents[2]
MODEL_PATH = BASE_DIR / "app" / "ml" / "resume_fit_model.pkl"
model_bundle: dict[str, Any] | None = None

def load_model() -> None:
    global model_bundle
    if not MODEL_PATH.exists():
        raise FileNotFoundError("Model file not found. Run: python app/ml/train_model.py")
    model_bundle = joblib.load(MODEL_PATH)

def analyze_resume_fit(resume_text: str, job_description: str) -> dict:
    if model_bundle is None: load_model()
    vectorizer = model_bundle["vectorizer"]
    model = model_bundle["model"]
    combined_text = resume_text + " [SEP] " + job_description
    combined_vector = vectorizer.transform([combined_text])
    prediction = model.predict(combined_vector)[0]
    confidence = float(max(model.predict_proba(combined_vector)[0]) * 100) if hasattr(model, "predict_proba") else 75.0
    resume_vector = vectorizer.transform([resume_text])
    job_vector = vectorizer.transform([job_description])
    similarity = float(cosine_similarity(resume_vector, job_vector)[0][0] * 100)
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)
    matched_skills = sorted(list(resume_skills.intersection(job_skills)))
    missing_skills = sorted(list(job_skills.difference(resume_skills)))
    skill_match_rate = (len(matched_skills) / len(job_skills) * 100) if job_skills else 0
    fit_score = round((similarity * 0.45) + (confidence * 0.30) + (skill_match_rate * 0.25), 2)
    return {"fit_category": prediction, "fit_score": fit_score, "confidence": round(confidence, 2), "skill_match_rate": round(skill_match_rate, 2), "matched_skills": matched_skills, "missing_skills": missing_skills, "suggestions": build_suggestions(missing_skills, prediction)}
