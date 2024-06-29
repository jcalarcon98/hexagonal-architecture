from dataclasses import dataclass

from app.users.domain import User


@dataclass
class CreateUserUseCaseResponse:
    user: User
