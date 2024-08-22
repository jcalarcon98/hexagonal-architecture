import typing

from dataclasses import dataclass
from app.users.domain import User


@dataclass
class GetUsersUseCaseResponse:
    users: typing.List[User]
