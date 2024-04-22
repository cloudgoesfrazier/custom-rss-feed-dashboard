from pydantic import BaseModel, Field, HttpUrl
from datetime import datetime

class FeedItem(BaseModel):
    title: str
    url: HttpUrl
    published: datetime
    summary: str = None  # Optional field

    class Config:
        schema_extra = {
            "example": {
                "title": "Example News Article",
                "url": "https://example.com/news",
                "published": "2024-04-01T12:00:00Z",
                "summary": "An example of a news article summary."
            }
        }
