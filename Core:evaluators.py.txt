from .models import Premise, Turn, Angle, Punch, Joke

class Evaluators:
    def score_premise(self, premise: Premise) -> float:
        # Premise tension should be moderately high in R4
        target = 0.7
        diff = abs(premise.tension - target)
        return max(0.0, 1.0 - diff)

    def score_turn(self, turn: Turn) -> float:
        return max(0.0, 1.0 - abs(turn.tension_shift - 0.3))

    def score_angle(self, angle: Angle) -> float:
        target = 0.65
        diff = abs(angle.absurdity - target)
        return max(0.0, 1.0 - diff)

    def score_punch(self, punch: Punch) -> float:
        target = 0.7
        diff = abs(punch.compression - target)
        return max(0.0, 1.0 - diff)

    def total(self, joke: Joke) -> float:
        scores = [
            self.score_premise(joke.premise),
            self.score_turn(joke.turn),
            self.score_angle(joke.angle),
            self.score_punch(joke.punch)
        ]
        return sum(scores) / len(scores)

