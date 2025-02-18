from pydantic import BaseModel


class UrlRequest(BaseModel):
    original_url: str
