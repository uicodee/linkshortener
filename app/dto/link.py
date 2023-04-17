from pydantic import BaseModel


class Link(BaseModel):

    title: str | None
    long_url: str
    short_url: str
    clicks: int


class ShortUrl(BaseModel):

    title: str | None
    short_url: str
    long_url: str
