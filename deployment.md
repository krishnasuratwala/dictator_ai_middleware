# Middleware Deployment (Render)

This folder contains the Flask Middleware (`server.py`) which manages users, payments, and connects to the GPU Node.

**Host**: Render.com (Web Service)

## 1. Setup on Render
1.  **New Web Service**.
2.  **Repo**: Select your GitHub repo.
3.  **Root Directory**: `middleware` (Important!)
4.  **Runtime**: Python 3.
5.  **Build Command**: `./render-build.sh` (or `pip install -r requirements.txt`)
6.  **Start Command**: `gunicorn server:app`

## 2. Environment Variables
Add these in the Render Dashboard:

| Key | Value |
| --- | --- |
| `PYTHON_VERSION` | `3.11.0` |
| `GPU_NODE_URL` | `http://[VAST_IP]:[PORT]/generate_stream` (e.g. `http://152.x.x.x:6000/generate_stream`) |
| `SECRET_KEY` | [Generate a random strong string] |
| `MONGO_URI` | [Your MongoDB Connection String] |

## 3. Important Note
*   This Middleware is now an **API Only** server.
*   It does **NOT** serve the Frontend files.
*   You do **NOT** need a `dist` folder here.
