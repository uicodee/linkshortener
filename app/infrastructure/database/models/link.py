from sqlalchemy import String, Column, BigInteger

from app.infrastructure.database.models.base import BaseModel


class Link(BaseModel):

    __tablename__ = "link"

    title = Column(String(length=255), nullable=False)
    long_url = Column(String, nullable=False)
    short_url = Column(String, nullable=False)
    clicks = Column(BigInteger, nullable=False, default=0)

