import typing

import pytest
from faker import Faker
from fastapi import FastAPI

from app.users.domain import User
from fastapi.testclient import TestClient

from app.users.domain.exceptions import UserNotFound
from app.users.domain.factories import get_user_by_id_case
from app.users.domain.ports.driver import GetUserByIdUseCase
from app.users.domain.ports.driver.get_user_by_id_use_case import (GetUserBydIdUseCaseRequest,
                                                                   GetUserBydIdUseCaseResponse)


@pytest.fixture
def client_factory(application: FastAPI) -> typing.Callable[..., TestClient]:
    def factory(get_user_by_id_use_case: typing.Callable[..., GetUserByIdUseCase]):
        application.dependency_overrides[get_user_by_id_case] = get_user_by_id_use_case
        return TestClient(application)
    yield factory
    application.dependency_overrides = {}


class TestGetUser:
    def test__should_return_a_user_not_found_exception(self, client_factory: typing.Callable[..., TestClient]) -> None:
        class FakeGetUserByIdUseCase(GetUserByIdUseCase):
            def handle(self, request: GetUserBydIdUseCaseRequest) -> GetUserBydIdUseCaseResponse:
                raise UserNotFound(error_message)

        error_message = "User not found"
        client = client_factory(get_user_by_id_use_case=FakeGetUserByIdUseCase)
        response = client.get(url="/users/123")

        assert response.status_code == 404
        assert response.json()["error_message"] == error_message

    def test__should_return_a_user_that_match_the_given_identifier(
        self,
        faker: Faker,
        client_factory: typing.Callable[..., TestClient]
    ) -> None:
        class FakeGetUserByIdUseCase(GetUserByIdUseCase):
            def handle(self, request: GetUserBydIdUseCaseRequest) -> GetUserBydIdUseCaseResponse:
                user = User(
                    identifier=request.identifier,
                    name=expected_data["name"],
                    lastname=expected_data["lastname"],
                    age=expected_data["age"],
                    email=expected_data["email"]
                )
                return GetUserBydIdUseCaseResponse(user=user)

        user_identifier = str(faker.uuid4())
        expected_data = {
            "identifier": user_identifier,
            "name": faker.name(),
            "lastname": faker.last_name(),
            "age": faker.pyint(min_value=1, max_value=90),
            "email": faker.email(),
        }
        client = client_factory(get_user_by_id_use_case=FakeGetUserByIdUseCase)
        response = client.get(url=f"/users/{user_identifier}")

        assert response.status_code == 200
        assert response.json() == expected_data
