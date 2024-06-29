from pydantic import BaseModel


class UserInput(BaseModel):
    name: str
    lastname: str
    email: str
    age: int
