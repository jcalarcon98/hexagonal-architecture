from uuid import uuid4

from app.domain.ports.driven import IdGenerator


class RandomIdGenerator(IdGenerator):
    def generate(self) -> str:
        return str(uuid4())
