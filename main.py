from fastapi import FastAPI
from models import UrlRequest
import random
import string

app = FastAPI()


url_mapping = {}


def generate_short_id(length=6):
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(length))


@app.post("/shorten")
async def create_short_url(request: UrlRequest):
    short_id = generate_short_id()
    url_mapping[short_id] = request.original_url
    return {"short_url": f"http://localhost:8000/{short_id}"}


@app.get("/{short_id}")
async def redirect_to_original_url(short_id: str):
    original_url = url_mapping.get(short_id)
    if original_url:
        return {"original_url": original_url}
    return {"error": "Short URL not found"}


@app.get("/")
async def root():
    return {"message": "Hello World"}
