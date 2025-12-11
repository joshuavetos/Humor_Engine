import random
from .models import Tag
from .persona import PERSONAS, DEFAULT_PERSONA

class TagEngine:
    def generate(self, persona: str, topic: str) -> Tag:
        profile = PERSONAS.get(persona, PERSONAS[DEFAULT_PERSONA])

        aggressive = profile.aggression
        absurd = profile.absurdity

        aggro_tags = [
            f"And if you disagree, congratulations — you’re part of the problem.",
            f"At this point, denial is the only real skill people bring to {topic}.",
        ]

        absurd_tags = [
            f"If {topic} had a mascot, it would be a raccoon in a business suit screaming.",
            f"{topic} functions on the same principles as haunted furniture.",
        ]

        dry_tags = [
            f"Statistically, none of this should surprise you.",
            f"There is no logical model in which {topic} succeeds.",
        ]

        pool = []
        pool += aggro_tags * int(aggressive * 3)
        pool += absurd_tags * int(absurd * 3)
        pool += dry_tags

        if not pool:
            pool = dry_tags

        num = random.choice([1, 2])
        chosen = random.sample(pool, k=min(num, len(pool)))

        return Tag(lines=chosen)

