from pydantic import BaseModel


class UserOutput(BaseModel):
    identifier: str
    name: str
    lastname: str
    age: int
    email: str
