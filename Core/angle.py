import random
from .models import Angle
from .persona import PERSONAS, DEFAULT_PERSONA
from .knowledge import KnowledgeBase

class AngleEngine:
    def __init__(self, kb: KnowledgeBase):
        self.kb = kb

    def generate(self, premise, turn):
        profile = PERSONAS.get(premise.persona, PERSONAS[DEFAULT_PERSONA])
        topic = premise.topic

        absurd = profile.absurdity
        aggressive = profile.aggression
        dry = profile.dryness

        absurd_angles = [
            f"It’s like if {topic} were designed by a committee of raccoons with head trauma.",
            f"{topic} works the same way a cult works — nobody agrees on anything but everyone shows up anyway.",
        ]

        aggressive_angles = [
            f"Honestly, {topic} feels like a social experiment they forgot to cancel.",
            f"{topic} only exists because nobody had the courage to admit it never worked.",
        ]

        dry_angles = [
            f"In the simplest terms, {topic} is just an inefficient exchange of disappointment.",
            f"Technically speaking, {topic} violates several basic principles of human competence.",
        ]

        neutral_angles = [
            f"The more you think about it, the more {topic} collapses under its own stupidity.",
            f"{topic} is just entropy in a costume pretending to have purpose.",
        ]

        pool = []
        pool += absurd_angles * int(absurd * 3)
        pool += aggressive_angles * int(aggressive * 3)
        pool += dry_angles * int(dry * 3)
        pool += neutral_angles

        if not pool:
            pool = neutral_angles

        text = random.choice(pool)
        absurdity = absurd + random.uniform(0.1, 0.3)

        return Angle(text=text, absurdity=absurdity, persona=profile.name)

