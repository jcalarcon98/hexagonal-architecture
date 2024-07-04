from dataclasses import dataclass


@dataclass
class User:
    identifier: str
    name: str
    lastname: str
    age: int
    email: str
