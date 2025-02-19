from pydantic import BaseModel, HttpUrl


class UrlRequest(BaseModel):
    original_url: HttpUrl
