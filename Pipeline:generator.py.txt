from humor_engine.core.compiler import JokeCompiler
from humor_engine.core.persona import PERSONAS

class HumorGenerator:
    def __init__(self, persona="observational"):
        self.persona = self._validate_persona(persona)
        self.compiler = JokeCompiler()

    def _validate_persona(self, p: str) -> str:
        p = str(p).lower().strip()
        if p not in PERSONAS:
            # Fallback to default
            return "observational"
        return p

    def generate(self, topic: str, style: str = "natural") -> str:
        # Normalize inputs
        clean_topic = str(topic).strip()
        clean_style = str(style).lower().strip()
        
        return self.compiler.compile(clean_topic, self.persona, clean_style)

