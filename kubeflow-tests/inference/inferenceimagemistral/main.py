from fastapi import FastAPI, Request
import requests

app = FastAPI()

OLLAMA_URL = "http://host.minikube.internal:11434/api/generate"

@app.post("/v1/models/ollama:predict")
async def predict(request: Request):
    body = await request.json()
    prompt = body.get("instances", [{}])[0].get("prompt", "")

    payload = {
        "model": "mistral",  # ou ce que tu as
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()

    output = response.json().get("response", "")
    return {"predictions": [output]}
