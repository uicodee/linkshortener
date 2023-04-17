from pydantic import BaseModel

from app.api.schems import types


class ShortUrl(BaseModel):

    long_url: str
    title: str
    utm_source: list[types.Tag] | None
