from dataclasses import dataclass


@dataclass
class CreateUserUseCaseRequest:
    name: str
    lastname: str
    email: str
    age: int
