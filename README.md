# Verifi-AI — Mock Prototype

This repository contains a static, mock prototype of Verifi-AI (formerly TrustLens) designed for hackathon submission.
It provides a frontend-only demo that simulates three key features:
- Text/URL verification
- Image screenshot (OCR simulation) verification
- Evidence & micro-lesson display

## Structure
- `frontend/index.html` — Static single-page demo. Open in browser or host via GitHub Pages.
- `backend/app.py` — Optional Flask mock server to serve `/analyze` responses (not required for GitHub Pages).
- `backend/requirements.txt` — Python dependency for optional mock server.

## How to publish to GitHub Pages (recommended)
1. Move `frontend/index.html` to repository root or `docs/` folder.
2. Push to GitHub.
3. In GitHub repo settings → Pages, select the branch and folder (`/root` or `/docs`) and save.
4. GitHub will publish the site at `https://<your-username>.github.io/<repo>/`.

## How to run optional mock backend locally
1. Install dependencies and run:
```
cd backend
python3 -m pip install -r requirements.txt
python app.py
```
2. The server will run on http://127.0.0.1:8080 and respond to POST /analyze requests.

## Demo instructions
- Use the "Use Example" button to load demo inputs and show canned outputs.
- For the submission, provide the GitHub Pages URL as the prototype link.

## Notes
This mock prototype is intentionally static to avoid requiring API keys or cloud setup during the hackathon. Replace with the full Cloud Run backend later for production.

