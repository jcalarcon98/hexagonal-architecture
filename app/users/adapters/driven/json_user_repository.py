import json
import typing

from app.users.domain import User
from app.users.domain.ports.driven import UserRepository


class JsonUserRepository(UserRepository):

    def __init__(self):
        self.json_path = "app/database/users.json"

    def get(self) -> typing.List[User]:
        with open(self.json_path, 'r') as users_file:
            users_info: typing.List[typing.Dict] = json.load(users_file)

        return [
            User(
                identifier=user_info["id"],
                name=user_info["name"],
                lastname=user_info["lastName"],
                age=user_info["age"],
                email=user_info["email"]
            )
            for user_info in users_info
        ]

    def get_by_id(self, identifier: str) -> typing.Optional[User]:
        with open(self.json_path, 'r') as users_file:
            users_info: typing.List[typing.Dict] = json.load(users_file)

        for user_info in users_info:
            if user_info["id"] == identifier:
                return User(
                    identifier=user_info["id"],
                    name=user_info["name"],
                    lastname=user_info["lastName"],
                    age=user_info["age"],
                    email=user_info["email"]
                )
        return None

    def create(self, user: User) -> User:
        created_user = User(
            identifier=user.identifier,
            name=user.name,
            lastname=user.lastname,
            age=user.age,
            email=user.email
        )
        return created_user
