import json
from pathlib import Path

class KnowledgeBase:
    def __init__(self, path="humor_engine/data/knowledge_base.json"):
        self.path = Path(path)
        if not self.path.exists():
            # If path doesn't exist, we warn or create empty structure, 
            # but ideally the data file should accompany the code.
            self.data = {"topics": {}, "violations": {}, "templates": {}}
        else:
            self.data = json.loads(self.path.read_text())

    def get_topic(self, topic: str):
        return self.data["topics"].get(topic.lower())

    def get_schemas(self, topic: str):
        entry = self.get_topic(topic)
        return entry["schemas"] if entry else []

    def get_concepts(self, topic: str):
        entry = self.get_topic(topic)
        return entry["concepts"] if entry else []

    def get_violations(self, schema: str):
        return self.data["violations"].get(schema, [])

