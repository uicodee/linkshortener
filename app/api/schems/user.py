from pydantic import BaseModel, Field


class LoginUser(BaseModel):

    email: str = Field(title="Email", description="User email", min_length=5, max_length=200)
    password: str = Field(title="Password", description="User password", min_length=6, max_length=50)


class RegisterUser(BaseModel):

    name: str = Field(title="Name", description="User name", min_length=1, max_length=50)
    email: str = Field(title="Email", description="User email", min_length=5, max_length=200)
    password: str = Field(title="Password", description="User password", min_length=6, max_length=50)