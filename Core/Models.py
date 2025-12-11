from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Premise:
    topic: str
    claim: str
    tension: float         # how much the audience would disagree
    persona: str

@dataclass
class Turn:
    text: str
    tension_shift: float   # decreases or increases audience resistance

@dataclass
class Angle:
    text: str
    absurdity: float       # how sideways the reasoning goes
    persona: str

@dataclass
class Punch:
    text: str
    compression: float     # how tightly the idea collapses into the punch

@dataclass
class Tag:
    lines: List[str]

@dataclass
class Joke:
    premise: Premise
    turn: Turn
    angle: Angle
    punch: Punch
    tags: Tag
    callback: Optional[str] = None

