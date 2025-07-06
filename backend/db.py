
import os
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()
MONGO_URL = os.getenv("MONGO_URL")
client = MongoClient(MONGO_URL)
db = client["VISION"]  # DB name
collection = db["results"]    # Collection name
def save_to_mongo(input_type, input_text, summary, questions):
    try:
        doc = {
            "input_type": input_type,
            "input_value": input_text[:500],  # Truncate large input
            "summary": summary,
            "questions": questions,
            "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        }
        collection.insert_one(doc)
        print("✅ Saved to MongoDB")
    except Exception as e:
        print("❌ Error saving to MongoDB:", str(e))
def fetch_recent(limit=10):
    try:
        return list(collection.find().sort("timestamp", -1).limit(limit))
    except Exception as e:
        print("❌ Failed to fetch history:", e)
        return []
