from pydantic import BaseModel, HttpUrl
from sqlalchemy import Column, Integer, String
from database import Base


# SQLAlchemy model for database
class URLMapping(Base):
    __tablename__ = "url_mapping"

    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String, nullable=False)
    short_id = Column(String, unique=True)


# Pydantic models for API
class URLBase(BaseModel):
    original_url: HttpUrl


class URLCreate(URLBase):
    pass


class URL(URLBase):
    id: int
    short_id: str
    original_url: str

    class Config:
        from_attributes = True
