import typing

import pytest
from faker import Faker

from app.users.adapters import MemoryUserRepository
from app.users.domain import User
from app.users.domain.exceptions import UserNotFound
from app.users.domain.ports import UserService
from app.users.domain.services import UserServiceImplementation


class TestUserService:
    @pytest.fixture
    def user_factory(self, faker: Faker) -> typing.Callable[..., User]:
        def factory() -> User:
            return User(
                identifier=faker.unique.pystr_format(string_format="##"),
                name=faker.name(),
                lastname=faker.last_name(),
                age=faker.random_int(min=1, max=99),
                email=faker.email()
            )
        return factory

    @pytest.fixture
    def user_service_dependencies(self) -> typing.Tuple[MemoryUserRepository, UserService]:
        user_repository = MemoryUserRepository()
        user_service: UserService = UserServiceImplementation(user_repository=user_repository)
        return user_repository, user_service

    def test__should_return_an_empty_users_array__when_there_are_no_users(
        self,
        user_service_dependencies: typing.Tuple[MemoryUserRepository, UserService]
    ) -> None:
        expected_response = []
        user_repository, user_service = user_service_dependencies

        users = user_service.get()

        assert len(users) == 0
        assert users == expected_response

    def test__should_return_all_users__when_it_is_called(
        self,
        user_factory: typing.Callable[..., User],
        user_service_dependencies: typing.Tuple[MemoryUserRepository, UserService]
    ) -> None:
        first_user = user_factory()
        second_user = user_factory()
        expected_response = [first_user, second_user]
        user_repository, user_service = user_service_dependencies
        user_repository.add_multiple([first_user, second_user])

        users = user_service.get()

        assert len(users) == len(expected_response)
        assert isinstance(users[0], User)
        assert users == expected_response

    def test__should_return_a_user_that_match_the_given_identifier(
        self,
        user_factory: typing.Callable[..., User],
        user_service_dependencies: typing.Tuple[MemoryUserRepository, UserService]
    ) -> None:
        expected_user = user_factory()
        user_repository, user_service = user_service_dependencies
        user_repository.add_multiple([expected_user])

        user = user_service.get_by_id(user_id=expected_user.identifier)

        assert isinstance(user, User)
        assert user == expected_user

    def test__should_raise_a_user_not_found_exception__when_the_user_with_the_given_identifier_does_not_exist(
        self,
        user_service_dependencies: typing.Tuple[MemoryUserRepository, UserService]
    ) -> None:
        wrong_identifier = "any-identifier"
        expected_exception_message = f"The user with the identifier {wrong_identifier} does not exist"
        user_repository, user_service = user_service_dependencies

        with pytest.raises(UserNotFound, match=expected_exception_message):
            user_service.get_by_id(user_id=wrong_identifier)
