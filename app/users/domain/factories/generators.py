from app.users.adapters.driven import RandomIdGenerator
from app.users.domain.ports.driven import IdGenerator


def get_id_generator() -> IdGenerator:
    return RandomIdGenerator()
