import random
from .models import Turn
from .persona import PERSONAS, DEFAULT_PERSONA
from .knowledge import KnowledgeBase

class TurnEngine:
    def __init__(self, kb: KnowledgeBase):
        self.kb = kb

    def generate(self, premise):
        profile = PERSONAS.get(premise.persona, PERSONAS[DEFAULT_PERSONA])
        
        topic = premise.topic
        info = self.kb.get_topic(topic)
        concepts = info["concepts"] if info else []

        base_turns = [
            f"Because every time you look at {topic}, all you see is {random.choice(concepts) if concepts else 'human dysfunction'}.",
            f"Because nothing about {topic} has ever functioned correctly in the history of the species.",
            f"Because deep down, everyone knows {topic} is just unresolved childhood trauma with extra steps.",
            f"Because {topic} only works if you ignore every red flag your instincts scream at you.",
        ]

        tension_shift = 0.2 + profile.aggression * 0.3 + profile.dryness * 0.1
        text = random.choice(base_turns)

        return Turn(text=text, tension_shift=tension_shift)

