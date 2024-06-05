import json
import typing
from typing import List

from app.users.entity import User


class UserRepository:

    def __init__(self):
        self.json_path = "app/database/users.json"

    def get(self) -> List[User]:
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

    def get_by_id(self, user_id: str) -> typing.Optional[User]:
        with open(self.json_path, 'r') as users_file:
            users_info: typing.List[typing.Dict] = json.load(users_file)

        for user_info in users_info:
            if user_info["id"] == user_id:
                return User(
                    identifier=user_info["id"],
                    name=user_info["name"],
                    lastname=user_info["lastName"],
                    age=user_info["age"],
                    email=user_info["email"]
                )
        return None
