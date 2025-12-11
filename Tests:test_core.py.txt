import pytest
import os
from pathlib import Path
from humor_engine.core.compiler import JokeCompiler
from humor_engine.pipeline.generator import HumorGenerator
from humor_engine.core.persona import PERSONAS

def test_unknown_persona_fallback():
    """Ensure invalid persona defaults to observational without crashing."""
    gen = HumorGenerator(persona="invalid_persona_string")
    assert gen.persona == "observational"
    joke = gen.generate("work")
    assert isinstance(joke, str)
    assert len(joke) > 10

def test_missing_topic_handling():
    """Ensure topics not in KB generate synthetic contrarian premises."""
    gen = HumorGenerator(persona="dark")
    # 'underwater_basket_weaving' is not in our JSON
    joke = gen.generate("underwater_basket_weaving")
    assert "Underwater_basket_weaving" in joke or "underwater_basket_weaving" in joke

def test_memory_persistence(tmp_path):
    """Test that memory writes to file and can be reloaded."""
    # Use a temp file for this test instance
    mem_file = tmp_path / "test_motifs.json"
    
    compiler = JokeCompiler(memory_path=str(mem_file))
    
    # Generate a joke (triggering a store)
    compiler.compile("airports", "dry")
    
    assert mem_file.exists()
    assert "timestamp" in mem_file.read_text()

def test_input_normalization():
    """Test API input normalization."""
    gen = HumorGenerator(persona="  DARK  ")
    assert gen.persona == "dark"
    
    # Pass messy style
    joke = gen.generate("dating", style="  MINIMAL  ")
    # Minimal style is short, usually one sentence
    assert len(joke) > 0

def test_concurrency_simulation(tmp_path):
    """Basic check that rapid writes don't crash the atomic writer."""
    mem_file = tmp_path / "concurrent_motifs.json"
    compiler = JokeCompiler(memory_path=str(mem_file))
    
    # Simulate 50 sequential writes (threading test would be more complex, 
    # but this verifies the logic doesn't lock itself out)
    for i in range(50):
        compiler.memory.store(f"joke {i}", 0.8)
        
    assert mem_file.exists()

