import typing
from uuid import uuid4

from app.users.domain.ports.driven import IdGenerator


class LocalIdGenerator(IdGenerator):
    def __init__(self):
        self.identifier: typing.Optional[str] = None

    def set_id_to_generate(self, identifier: str) -> None:
        self.identifier = identifier

    def generate(self) -> str:
        return self.identifier or str(uuid4())
