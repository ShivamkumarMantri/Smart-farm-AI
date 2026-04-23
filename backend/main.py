import os
import json
from pathlib import Path
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import shutil

from services.hybrid_predictor import hybrid_predict

app = FastAPI(title="SmartFarm AI Backend API")

# Configure CORS for Vite React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For dev, allow all. In prod, lock this down.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = Path("data/uploads")
MEMORY_FILE = Path("data/memory/embeddings.json")

# Ensure directories exist
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)

@app.post("/api/predict")
async def predict(
    file: UploadFile = File(...),
    userCrop: str = Form(None),
    forceGemini: bool = Form(False)
):
    # Save the file temporarily
    file_path = UPLOAD_DIR / file.filename
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    try:
        # Run prediction
        result = hybrid_predict(
            str(file_path),
            user_crop=userCrop if userCrop and userCrop.strip() != "" else None,
            force_gemini=forceGemini
        )
        return {"success": True, "result": result}
    except Exception as e:
        return {"success": False, "error": str(e)}

@app.get("/api/history")
async def get_history():
    if not MEMORY_FILE.exists():
        return {"success": True, "history": []}
    
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        # Format history into a list sorted by time
        history_list = []
        for id, item in data.items():
            entry = item.copy()
            entry["id"] = id
            history_list.append(entry)
            
        # Sort newest first
        history_list.sort(key=lambda x: x.get("timestamp", ""), reverse=True)
        return {"success": True, "history": history_list}
    except Exception as e:
        return {"success": False, "error": str(e)}

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
