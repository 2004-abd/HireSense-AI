from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import MONGO_URI, MONGO_DB

client = AsyncIOMotorClient(MONGO_URI)
db = client[MONGO_DB]

users_collection = db["users"]
analyses_collection = db["analyses"]
metrics_collection = db["model_metrics"]
logs_collection = db["system_logs"]
