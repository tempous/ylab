from pydantic import BaseModel, EmailStr

__all__ = ("Signup","Login","Tokens",)


class Tokens(BaseModel):
    access_token: str
    refresh_token: str


class Logout(BaseModel):
    refresh_token: str


class Login(BaseModel):
    username: str
    password: str


class Signup(Login):
    email: EmailStr
