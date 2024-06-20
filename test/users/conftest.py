import typing
import pytest
from faker import Faker

from app.users.domain import User


@pytest.fixture
def user_factory(faker: Faker) -> typing.Callable[..., User]:
    def factory(**kwargs: typing.Dict[str, typing.Any]) -> User:
        user_fields = {
            "identifier": str(faker.uuid4()),
            "name": faker.name(),
            "lastname": faker.last_name(),
            "age": faker.random_int(min=1, max=99),
            "email": faker.email(),
            **kwargs
        }
        return User(**user_fields)
    return factory
