from fastapi import FastAPI
from pydantic import BaseModel, validator
from humor_engine.pipeline.generator import HumorGenerator
from humor_engine.core.persona import PERSONAS

app = FastAPI()

class JokeRequest(BaseModel):
    topic: str
    persona: str = "observational"
    style: str = "natural"

    @validator('persona')
    def validate_persona(cls, v):
        v = v.lower().strip()
        if v not in PERSONAS:
            return "observational"  # Safe fallback
        return v

    @validator('topic')
    def validate_topic(cls, v):
        return v.strip()

@app.get("/")
def home():
    return {"status": "HumorEngine v2.1 online"}

@app.post("/generate")
def generate(req: JokeRequest):
    # Generator handles the logic, validations ensure clean inputs
    generator = HumorGenerator(persona=req.persona)
    joke = generator.generate(req.topic, style=req.style)
    
    return {
        "topic": req.topic,
        "persona": req.persona,
        "style": req.style,
        "joke": joke
    }

