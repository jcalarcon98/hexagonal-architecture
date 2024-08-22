import typing

import pytest
from faker import Faker

from fastapi.testclient import TestClient

from app.users.domain import User
from fastapi import FastAPI
from app.users.domain.ports.driver import CreateUserUseCase
from app.users.domain.factories import create_user_case
from app.users.domain.ports.driver.create_user_use_case import CreateUserUseCaseRequest, CreateUserUseCaseResponse


@pytest.fixture
def client_factory(application: FastAPI) -> typing.Callable[..., TestClient]:
    def factory(create_user_use_case: typing.Callable[..., CreateUserUseCase]):
        application.dependency_overrides[create_user_case] = create_user_use_case
        return TestClient(application)
    yield factory
    application.dependency_overrides = {}


class TestCreateUser:
    def test__should_create_a_new_user_when_it_is_called(
        self,
        faker: Faker,
        client_factory
    ) -> None:

        class FakeCreateUserUseCase(CreateUserUseCase):
            def handle(self, request: CreateUserUseCaseRequest):
                return CreateUserUseCaseResponse(
                    user=User(**expected_data)
                )

        expected_data = {
            "identifier": str(faker.uuid4()),
            "name": faker.name(),
            "lastname": faker.last_name(),
            "age": faker.pyint(min_value=1, max_value=90),
            "email": faker.email()
        }

        client = client_factory(create_user_use_case=FakeCreateUserUseCase)
        response = client.post(url="/users", json={
            "name": expected_data["name"],
            "lastname": expected_data["lastname"],
            "age": expected_data["age"],
            "email": expected_data["email"]
        })

        assert response.status_code == 200
        assert response.json() == expected_data
