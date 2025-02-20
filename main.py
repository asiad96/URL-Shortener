from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from models import UrlRequest
from database import SessionLocal, UrlMapping
import random
import string

app = FastAPI()


def generate_short_id(length=6):
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(length))


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/shorten")
async def create_short_url(request: UrlRequest, db: Session = Depends(get_db)):
    short_id = generate_short_id()
    db_url = UrlMapping(original_url=request.original_url, short_id=short_id)
    db.add(db_url)
    db.commit()
    return {"short_url": db_url.short_id}


@app.get("/{short_id}")
async def redirect_to_original_url(short_id: str, db: Session = Depends(get_db)):
    db_url = db.query(UrlMapping).filter(UrlMapping.short_id == short_id).first()
    if db_url:
        return {"original_url": db_url.original_url}
    raise HTTPException(status_code=404, detail="Short URL not found")


@app.get("/")
async def root():
    return {"message": "Hello World"}
