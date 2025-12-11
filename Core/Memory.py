import json
import time
import math
import threading
import os
from pathlib import Path
from dataclasses import dataclass, asdict

@dataclass
class Motif:
    text: str
    score: float
    timestamp: float

class CallbackMemory:
    def __init__(self, path="humor_engine/data/motifs.json"):
        self.path = Path(path)
        self.lock = threading.Lock()
        
        # Ensure parent dir exists
        if not self.path.parent.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            
        if not self.path.exists():
            self._write_file([])

        self.motifs = []
        self._load()

    def _load(self):
        """Load motifs into memory protected by lock."""
        with self.lock:
            try:
                if self.path.exists():
                    data = json.loads(self.path.read_text())
                else:
                    data = []
            except (json.JSONDecodeError, OSError):
                data = []
            self.motifs = [Motif(**m) for m in data]

    def store(self, text: str, score: float):
        """Thread-safe store with atomic file write."""
        with self.lock:
            motif = Motif(text=text, score=score, timestamp=time.time())
            self.motifs.append(motif)
            
            # Simple exponential decay cleanup if too large
            if len(self.motifs) > 100:
                self.motifs = sorted(self.motifs, key=lambda m: m.timestamp)[-50:]
            
            self._save_safe()

    def _save_safe(self):
        """Atomic write pattern: write to tmp, then replace."""
        data = [asdict(m) for m in self.motifs]
        json_str = json.dumps(data, indent=2)
        
        tmp_path = self.path.with_suffix(".tmp")
        try:
            tmp_path.write_text(json_str)
            # Atomic replace (POSix-compliant, mostly works on Windows too)
            tmp_path.replace(self.path)
        except OSError:
            # Fallback if replace fails
            if tmp_path.exists():
                os.remove(tmp_path)

    def _write_file(self, data):
        self.path.write_text(json.dumps(data, indent=2))

    def activation(self, motif: Motif) -> float:
        """Exponential decay activation for callback timing."""
        decay = 0.06
        minutes = (time.time() - motif.timestamp) / 60

        if minutes < 1:
            return 0.0

        return motif.score * math.exp(-decay * minutes)

    def best(self):
        """Thread-safe read of best motif."""
        with self.lock:
            if not self.motifs:
                return None
            
            # Copy motifs to avoid mutation during iteration if threading gets complex
            current_motifs = list(self.motifs)

        scored = [(m, self.activation(m)) for m in current_motifs]
        viable = [(m, s) for m, s in scored if s > 0.3]

        if not viable:
            return None

        best, _ = max(viable, key=lambda x: x[1])
        minutes = int((time.time() - best.timestamp) / 60)
        return f"Remember {minutes} minutes ago? {best.text}"

