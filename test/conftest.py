import pytest
from fastapi import FastAPI
from faker import Faker

from main import app


@pytest.fixture
def application() -> FastAPI:
    return app


@pytest.fixture
def create_fake_user_factory():
    faker = Faker()

    def factory():
        return {
            "identifier": str(faker.uuid4()),
            "name": faker.name(),
            "lastname": faker.last_name(),
            "age": faker.pyint(min_value=1, max_value=90),
            "email": faker.email(),
        }
    return factory



