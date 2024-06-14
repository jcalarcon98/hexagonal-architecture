from pydantic import BaseModel


class User(BaseModel):
    name: str
    lastname: str
    email: str
    age: int
