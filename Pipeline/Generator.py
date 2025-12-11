from typing import Optional
from humor_engine.core.compiler import JokeCompiler
from humor_engine.core.persona import safe_persona

class HumorGenerator:
    def __init__(self, persona="observational", compiler: Optional[JokeCompiler] = None):
        # Allow injection of shared compiler to avoid reloading KB
        self.compiler = compiler if compiler else JokeCompiler()
        
        # Ensure persona is valid immediately
        profile = safe_persona(persona)
        self.persona = profile.name

    def generate(self, topic: str, style: str = "natural") -> str:
        clean_topic = str(topic).strip()
        clean_style = str(style).lower().strip()
        
        return self.compiler.compile(clean_topic, self.persona, clean_style)


