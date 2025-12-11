HumorEngine v2.1
A modular, cognitive stand-up comedy engine. v2.1 includes production hardening, thread safety, and unified knowledge management.
🛠 Setup
pip install -r requirements.txt

🚀 Running
API Server:
uvicorn humor_engine.pipeline.server:app --reload

CLI:
python main.py

🧪 Testing
pytest tests/

⚡ Key Improvements (v2.1)
• Thread Safety: Atomic file writes and locking for motifs.json.
• Performance: KnowledgeBase is loaded once per process, not per request.
• Robustness: Safe KeyError handling for unknown personas; input validation in API.
• Packaging: Dockerfile and requirements.txt included for reproducible builds.
