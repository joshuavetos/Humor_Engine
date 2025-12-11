class PersonaProfile:
    def __init__(self, name, 
                 contrarian_weight,
                 absurdity_weight,
                 aggression_weight,
                 dryness_weight,
                 emotional_weight):
        self.name = name
        self.contrarian = contrarian_weight
        self.absurdity = absurdity_weight
        self.aggression = aggression_weight
        self.dryness = dryness_weight
        self.emotion = emotional_weight

PERSONAS = {
    "dark": PersonaProfile("dark", 0.8, 0.3, 0.7, 0.4, 0.8),
    "chaotic": PersonaProfile("chaotic", 0.6, 1.0, 0.4, 0.2, 0.6),
    "dry": PersonaProfile("dry", 0.5, 0.1, 0.2, 1.0, 0.2),
    "aggressive": PersonaProfile("aggressive", 0.9, 0.3, 1.0, 0.3, 0.7),
    "observational": PersonaProfile("observational", 0.4, 0.2, 0.3, 0.6, 0.5),
}

DEFAULT_PERSONA = "observational"

def safe_persona(name: str) -> PersonaProfile:
    """Safe lookup wrapper ensuring a valid PersonaProfile is always returned."""
    if not isinstance(name, str):
        return PERSONAS[DEFAULT_PERSONA]
    return PERSONAS.get(name.lower().strip(), PERSONAS[DEFAULT_PERSONA])


