# ──────────────────────────────────────────
#  slizzai_app.py - Finalized
# ──────────────────────────────────────────
import json
import uuid
import asyncio
import logging
from datetime import datetime
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional

import torch
from PIL import Image
from diffusers import StableDiffusionPipeline, StableDiffusionXLPipeline
from transformers import pipeline

from fastapi import FastAPI, Request, UploadFile, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy import Column, DateTime, Float, String, Text, create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker
from pydantic import BaseModel, Field
from enum import Enum

# ──────────────────────────────────────────
#  Logging Setup
# ──────────────────────────────────────────
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("slizzai")

# ──────────────────────────────────────────
#  Configuration & Paths
# ──────────────────────────────────────────
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
ROOT_DIR = Path(__file__).parent
DB_URL = f"sqlite:///{ROOT_DIR / 'slizzai.db'}"

engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# ──────────────────────────────────────────
#  Enums & Constants
# ──────────────────────────────────────────
class JobStatus(str, Enum):
    QUEUED = "queued"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"

# ──────────────────────────────────────────
#  Database Models
# ──────────────────────────────────────────
class UserSession(Base):
    __tablename__ = "user_sessions"
    user_id = Column(String, primary_key=True, index=True)
    session_token = Column(String, unique=True)
    preferences = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    last_active = Column(DateTime, default=datetime.utcnow)

class GenerationJob(Base):
    __tablename__ = "generation_jobs"
    job_id = Column(String, primary_key=True, index=True)
    user_id = Column(String)
    prompt = Column(Text)
    status = Column(String, index=True)
    result_path = Column(String)
    parameters = Column(Text)
    pnqi_score = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
    completed_at = Column(DateTime, nullable=True)

Base.metadata.create_all(bind=engine)

# ──────────────────────────────────────────
#  Models & Helpers
# ──────────────────────────────────────────
@dataclass
class StyleVector:
    palette: List[str]
    texture: str
    emotion: str
    composition: str
    lighting: str
    signature_elements: List[str]
    controlnet_params: Dict[str, float]
    lora_weights: Dict[str, float]
    mode: Optional[str] = "balanced"

class GenerationRequest(BaseModel):
    prompt: str = Field(..., example="A cinematic photo of Utica NY at dusk")
    negative_prompt: str = "low quality, blurry"
    width: int = 768
    height: int = 768
    steps: int = 50
    guidance_scale: float = 7.5
    seed: Optional[int] = None
    model_type: Optional[str] = None  # e.g., "sdxl" or "sd21"

class PromptEngine:
    def __init__(self) -> None:
        self._sentiment = pipeline("sentiment-analysis")

    def analyze(self, text: str) -> Dict[str, float]:
        sentiment = self._sentiment(text)[0]
        pnqi = min(10.0, len(text.split()) * 0.2 + sentiment["score"] * 2)
        return {"sentiment": sentiment, "pnqi_score": round(pnqi, 2)}

prompt_engine = PromptEngine()

class StyleFingerprint:
    def __init__(self, user_id: str, db: Session) -> None:
        self.user_id = user_id
        self.db = db

    def load(self) -> StyleVector:
        row = self.db.query(UserSession).filter_by(user_id=self.user_id).first()
        if row and row.preferences:
            return StyleVector(**json.loads(row.preferences))
        default = StyleVector(
            palette=["#FF4EFF", "#1AB8F5", "#0D0D0F", "#F0F8FF", "#FFD700"],
            texture="photorealistic and finely detailed",
            emotion="balanced, dynamic",
            composition="rule of thirds, depth",
            lighting="natural light with dramatic shadows",
            signature_elements=["atmospheric effects", "color harmony", "texture contrast"],
            controlnet_params=dict(canny_strength=0.8, depth_strength=0.6, pose_strength=0.9),
            lora_weights=dict(style_enhance=0.8, detail_boost=0.6, color_pop=0.4),
        )
        self.save(default)
        return default

    def save(self, vector: StyleVector) -> None:
        row = self.db.query(UserSession).filter_by(user_id=self.user_id).first()
        if not row:
            row = UserSession(user_id=self.user_id, session_token=str(uuid.uuid4()))
            self.db.add(row)
        row.preferences = json.dumps(asdict(vector))
        row.last_active = datetime.utcnow()
        self.db.commit()

class ModelManager:
    _lock = asyncio.Lock()
    _pipes: Dict[str, StableDiffusionPipeline] = {}

    @classmethod
    async def _load(cls, name: str) -> StableDiffusionPipeline:
        async with cls._lock:
            if name in cls._pipes:
                return cls._pipes[name]
            model_map = {
                "sdxl": ("stabilityai/stable-diffusion-xl-base-1.0", StableDiffusionXLPipeline),
                "sd21": ("stabilityai/stable-diffusion-2-1", StableDiffusionPipeline)
            }
            model_id, klass = model_map.get(name, model_map["sd21"])
            pipe = klass.from_pretrained(
                model_id,
                torch_dtype=torch.float16 if DEVICE == "cuda" else torch.float32
            ).to(DEVICE)
            if hasattr(pipe, "enable_memory_efficient_attention"):
                pipe.enable_memory_efficient_attention()
            cls._pipes[name] = pipe
            return pipe

    @classmethod
    async def generate(cls, req: GenerationRequest, style: StyleVector) -> Image.Image:
        pipe_name = req.model_type or ("sdxl" if req.width > 768 or req.height > 768 else "sd21")
        pipe = await cls._load(pipe_name)
        prompt = f"{req.prompt}, {style.emotion}, {style.texture}, {style.lighting}"
        generator = torch.Generator(device=DEVICE).manual_seed(req.seed or uuid.uuid4().int % 2**32)
        with torch.autocast(device_type=DEVICE):
            result = pipe(
                prompt=prompt,
                negative_prompt=req.negative_prompt,
                width=req.width,
                height=req.height,
                num_inference_steps=req.steps,
                guidance_scale=req.guidance_scale,
                generator=generator,
            )
        return result.images[0]
    # ──────────────────────────────────────────
#  FastAPI Ritual Routes
# ──────────────────────────────────────────
app = FastAPI(title="SlizzAi", version="1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = ROOT_DIR / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)

@app.post("/generate")
async def generate_image(req: GenerationRequest):
    db = SessionLocal()
    user_id = "default_user"  # Replace with real auth/session logic if needed

    # Analyze prompt
    analysis = prompt_engine.analyze(req.prompt)
    pnqi_score = analysis["pnqi_score"]

    # Load style
    fingerprint = StyleFingerprint(user_id, db)
    style = fingerprint.load()

    # Generate image
    try:
        image = await ModelManager.generate(req, style)
    except Exception as e:
        logger.error(f"Generation failed: {e}")
        return JSONResponse(status_code=500, content={"error": "Image generation failed."})

    # Save image
    job_id = str(uuid.uuid4())
    filename = f"{job_id}.png"
    image_path = UPLOAD_DIR / filename
    image.save(image_path)

    # Log job
    job = GenerationJob(
        job_id=job_id,
        user_id=user_id,
        prompt=req.prompt,
        status=JobStatus.COMPLETED,
        result_path=str(image_path),
        parameters=req.json(),
        pnqi_score=pnqi_score,
        created_at=datetime.utcnow(),
        completed_at=datetime.utcnow()
    )
    db.add(job)
    db.commit()

    return {
        "job_id": job_id,
        "pnqi_score": pnqi_score,
        "result_url": f"/uploads/{filename}",
        "style_used": asdict(style),
        "prompt_enriched": f"{req.prompt}, {style.emotion}, {style.texture}, {style.lighting}"
    }

@app.get("/style")
def get_style(user_id: str = "default_user"):
    db = SessionLocal()
    fingerprint = StyleFingerprint(user_id, db)
    style = fingerprint.load()
    return asdict(style)

@app.get("/analyze")
def analyze_prompt(prompt: str):
    return prompt_engine.analyze(prompt)

# ──────────────────────────────────────────
#  Static File Serving
# ──────────────────────────────────────────
from fastapi.staticfiles import StaticFiles
app.mount("/uploads", StaticFiles(directory=UPLOAD_DIR), name="uploads")