from .knowledge import KnowledgeBase
from .premise import PremiseEngine
from .turn import TurnEngine
from .angle import AngleEngine
from .punch import PunchlineEngine
from .tag import TagEngine
from .delivery import DeliveryEngine
from .evaluators import Evaluators
from .memory import CallbackMemory
from .models import Joke

class JokeCompiler:
    def __init__(self, memory_path="humor_engine/data/motifs.json"):
        # 1. Instantiate shared KnowledgeBase ONCE
        self.kb = KnowledgeBase()
        
        # 2. Inject KB into engines
        self.premise_engine = PremiseEngine(self.kb)
        self.turn_engine = TurnEngine(self.kb)
        self.angle_engine = AngleEngine(self.kb)
        
        self.punch_engine = PunchlineEngine()
        self.tag_engine = TagEngine()
        self.delivery = DeliveryEngine()
        self.evaluators = Evaluators()
        
        # 3. Configurable memory path for testing isolation
        self.memory = CallbackMemory(path=memory_path)

    def compile(self, topic: str, persona: str, style: str = "natural") -> str:
        # 1. Generate cognitive components
        premise = self.premise_engine.generate(topic, persona)
        turn = self.turn_engine.generate(premise)
        angle = self.angle_engine.generate(premise, turn)
        punch = self.punch_engine.generate(premise, turn, angle)
        tags = self.tag_engine.generate(persona, topic)

        # 2. Construct Joke object
        joke_obj = Joke(premise, turn, angle, punch, tags)

        # 3. Evaluate & Store
        score = self.evaluators.total(joke_obj)
        self.memory.store(punch.text, score)

        # 4. Callback logic
        callback = self.memory.best()
        joke_obj.callback = callback

        # 5. Deliver
        return self.delivery.deliver(joke_obj, style=style)

