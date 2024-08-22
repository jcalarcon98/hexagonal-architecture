import typing

import pytest

from app.users.adapters.driven import MemoryUserRepository
from app.users.domain import User
from app.users.domain.cases import GetUserByIdCase
from app.users.domain.exceptions import UserNotFound
from app.users.domain.ports.driver import GetUserByIdUseCase
from app.users.domain.ports.driver.get_user_by_id_use_case import GetUserBydIdUseCaseRequest


class TestGetUserByIdCase:
    @pytest.fixture
    def get_users_case_dependencies(self) -> typing.Tuple[GetUserByIdUseCase, MemoryUserRepository]:
        memory_user_repository = MemoryUserRepository()
        get_user_by_id_case: GetUserByIdUseCase = GetUserByIdCase(user_repository=memory_user_repository)
        return get_user_by_id_case, memory_user_repository

    def test__should_return_a_user_that_match_the_given_identifier(
        self,
        user_factory: typing.Callable[..., User],
        get_users_case_dependencies: typing.Tuple[GetUserByIdCase, MemoryUserRepository]
    ) -> None:
        expected_user = user_factory()
        get_user_by_id_case, user_repository = get_users_case_dependencies
        user_repository.add_multiple([expected_user])

        get_user_by_id_case_request = GetUserBydIdUseCaseRequest(
            identifier=expected_user.identifier
        )

        response = get_user_by_id_case.handle(request=get_user_by_id_case_request)
        user = response.user

        assert isinstance(user, User)
        assert user == expected_user

    def test__should_raise_a_user_not_found_exception__when_the_user_with_the_given_identifier_does_not_exist(
        self,
        get_users_case_dependencies: typing.Tuple[GetUserByIdCase, MemoryUserRepository]
    ) -> None:
        wrong_identifier = "any-identifier"
        get_user_by_id_case_request = GetUserBydIdUseCaseRequest(
            identifier=wrong_identifier
        )
        expected_exception_message = f"The user with the identifier {wrong_identifier} does not exist"
        get_user_by_id_case, user_repository = get_users_case_dependencies

        with pytest.raises(UserNotFound, match=expected_exception_message):
            get_user_by_id_case.handle(request=get_user_by_id_case_request)
