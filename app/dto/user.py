from app.dto import Base


class User(Base):

    name: str
    email: str


class PasswordUser(Base):

    name: str
    email: str
    password: str
