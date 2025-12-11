import random
from .models import Premise
from .knowledge import KnowledgeBase
from .persona import PERSONAS, DEFAULT_PERSONA

class PremiseEngine:
    def __init__(self, kb: KnowledgeBase):
        self.kb = kb

    def generate(self, topic: str, persona: str) -> Premise:
        # Safe access with default fallback
        profile = PERSONAS.get(persona, PERSONAS[DEFAULT_PERSONA])
        info = self.kb.get_topic(topic)

        # If no dataset entry: synthetic contrarian premise
        if not info:
            claim = f"{topic.capitalize()} is proof humans stopped evolving emotionally."
            tension = 0.7 + profile.aggression * 0.2
            return Premise(topic, claim, tension, profile.name)

        schema = random.choice(info["schemas"])
        concept = random.choice(info["concepts"])

        base_claims = [
            f"{topic.capitalize()} isn’t about {schema} — it’s emotional tax fraud.",
            f"{topic.capitalize()} only exists because humans refuse therapy.",
            f"{topic.capitalize()} is just {concept} cosplay with paperwork.",
            f"{topic.capitalize()} was invented to punish optimism.",
        ]

        intensity = profile.aggression + profile.contrarian * 0.5
        claim = random.choice(base_claims)
        tension = min(1.0, 0.5 + intensity * 0.5)

        return Premise(topic, claim, tension, profile.name)

