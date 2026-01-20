# Streamlit app (web.app.py)

This branch adds a simple Streamlit demo app that calls Google GenAI.

Files added:
- web.app.py — Streamlit application
- requirements.txt — contains streamlit and google-genai
- STREAMLIT_RUN.md — instructions to run the app

How to run locally

1. Create and activate a virtual environment (recommended):
   - python -m venv .venv
   - source .venv/bin/activate  (macOS / Linux) or .venv\Scripts\Activate.ps1 (Windows PowerShell)

2. Install dependencies:
   - python -m pip install --upgrade pip
   - pip install -r requirements.txt

3. Set credentials (one of these):
   - export GOOGLE_API_KEY="YOUR_API_KEY"  (Linux/macOS)
   - setx GOOGLE_API_KEY "YOUR_API_KEY"  (Windows, then restart terminal)
   or set GOOGLE_APPLICATION_CREDENTIALS to the path to a service account JSON file:
   - export GOOGLE_APPLICATION_CREDENTIALS="/path/to/key.json"

4. Run the Streamlit app:
   - streamlit run web.app.py

Notes
- The app will also accept an API key entered into the optional field in the UI (not recommended for production).
- The google-genai client library has changed over time; if you get attribute errors, inspect the client object to find the correct call shape.

