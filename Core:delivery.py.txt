from .models import Joke

class DeliveryEngine:
    def structured(self, joke: Joke) -> str:
        """Full 5-stage breakdown plus optional callback."""
        out = []
        out.append(f"PREMISE: {joke.premise.claim}")
        out.append(f"TURN: {joke.turn.text}")
        out.append(f"ANGLE: {joke.angle.text}")
        out.append(f"PUNCH: {joke.punch.text}")
        
        if joke.tags.lines:
            for t in joke.tags.lines:
                out.append(f"TAG: {t}")

        if joke.callback:
            out.append(f"CALLBACK: {joke.callback}")

        return "\n".join(out)

    def natural(self, joke: Joke) -> str:
        """Compressed stand-up delivery."""
        parts = [
            joke.premise.claim,
            joke.turn.text,
            joke.angle.text,
            joke.punch.text,
        ]
        parts.extend(joke.tags.lines)

        if joke.callback:
            parts.append(joke.callback)

        return " ".join(parts)

    def minimal(self, joke: Joke) -> str:
        """Punchline-only output (useful for testing)."""
        return joke.punch.text

    def deliver(self, joke: Joke, style: str = "natural") -> str:
        style = style.lower().strip()
        if style == "structured":
            return self.structured(joke)
        if style == "minimal":
            return self.minimal(joke)
        return self.natural(joke)

