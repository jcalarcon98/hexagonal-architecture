import typing
import pytest

from app.users.adapters.driven import MemoryUserRepository
from app.users.domain import User
from app.users.domain.cases import GetUsersCase
from app.users.domain.ports.driver import GetUsersUseCase


class TestGetUsersCase:
    @pytest.fixture
    def get_users_case_dependencies(self) -> typing.Tuple[GetUsersUseCase, MemoryUserRepository]:
        memory_user_repository = MemoryUserRepository()
        get_users_case: GetUsersUseCase = GetUsersCase(user_repository=memory_user_repository)
        return get_users_case, memory_user_repository

    def test__should_return_an_empty_users_array__when_there_are_no_users(
        self,
        get_users_case_dependencies: typing.Tuple[GetUsersUseCase, MemoryUserRepository]
    ) -> None:
        expected_response = []
        get_users_case, _ = get_users_case_dependencies

        response = get_users_case.handle()
        users = response.users

        assert len(users) == 0
        assert users == expected_response

    def test__should_return_all_users__when_it_is_called(
        self,
        user_factory: typing.Callable[..., User],
        get_users_case_dependencies: typing.Tuple[GetUsersUseCase, MemoryUserRepository]
    ) -> None:
        first_user = user_factory()
        second_user = user_factory()
        expected_response = [first_user, second_user]
        get_users_case, user_repository = get_users_case_dependencies
        user_repository.add_multiple([first_user, second_user])

        response = get_users_case.handle()
        users = response.users

        assert len(users) == len(expected_response)
        assert isinstance(users[0], User)
        assert users == expected_response
