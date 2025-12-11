import random
from .models import Punch
from .persona import PERSONAS, DEFAULT_PERSONA

class PunchlineEngine:
    def generate(self, premise, turn, angle):
        profile = PERSONAS.get(premise.persona, PERSONAS[DEFAULT_PERSONA])
        topic = premise.topic

        base_punches = [
            f"So yeah — {topic} isn’t broken. It’s functioning exactly as designed: terribly.",
            f"In the end, {topic} isn’t a process — it’s a cry for help wearing a lanyard.",
            f"{topic} isn’t complicated. It’s just stupidity with branding.",
            f"{topic} only feels normal because everyone agreed to stop asking questions.",
        ]

        compression_level = (
            0.4
            + profile.aggression * 0.3
            + profile.absurdity * 0.2
            + random.uniform(0.05, 0.15)
        )

        text = random.choice(base_punches)
        return Punch(text=text, compression=compression_level)

