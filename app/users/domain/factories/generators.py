from app.adapters.driven import RandomIdGenerator
from app.domain.ports.driven import IdGenerator


def get_id_generator() -> IdGenerator:
    return RandomIdGenerator()
