from sqlalchemy import Column, String

from app.infrastructure.database.models.base import BaseModel


class User(BaseModel):

    __tablename__ = "user"

    name = Column(String(length=255), nullable=False)
    email = Column(String(length=255), nullable=False)
    password = Column(String, nullable=False)

    def __str__(self):
        return f"{self.name}\n" \
               f"{self.email}\n" \
               f"{self.password}\n"
