import typing

import pytest
from faker import Faker

from app.users.adapters.driven import (
    MemoryUserRepository,
    LocalNotificationService,
    LocalIdGenerator
)
from app.users.domain import User
from app.users.domain.exceptions import UserNotFound, UserAlreadyExists
from app.users.domain.ports.driver import UserService
from app.users.domain.services import UserServiceImplementation


class TestUserService:
    @pytest.fixture
    def user_factory(self, faker: Faker) -> typing.Callable[..., User]:
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

    @pytest.fixture
    def user_service_dependencies(self) -> typing.Tuple[
        UserService, MemoryUserRepository, LocalNotificationService, LocalIdGenerator
    ]:
        memory_user_repository = MemoryUserRepository()
        console_notification_service = LocalNotificationService()
        local_id_generator = LocalIdGenerator()
        user_service: UserService = UserServiceImplementation(
            user_repository=memory_user_repository,
            notification_service=console_notification_service,
            id_generator=local_id_generator
        )
        return user_service, memory_user_repository, console_notification_service, local_id_generator

    def test__should_return_an_empty_users_array__when_there_are_no_users(
        self,
        user_service_dependencies: typing.Tuple[
            UserService, MemoryUserRepository, LocalNotificationService, LocalIdGenerator
        ]
    ) -> None:
        expected_response = []
        user_service, user_repository, _, _ = user_service_dependencies

        users = user_service.get()

        assert len(users) == 0
        assert users == expected_response

    def test__should_return_all_users__when_it_is_called(
        self,
        user_factory: typing.Callable[..., User],
        user_service_dependencies: typing.Tuple[
            UserService, MemoryUserRepository, LocalNotificationService, LocalIdGenerator
        ]
    ) -> None:
        first_user = user_factory()
        second_user = user_factory()
        expected_response = [first_user, second_user]
        user_service, user_repository, _, _ = user_service_dependencies
        user_repository.add_multiple([first_user, second_user])

        users = user_service.get()

        assert len(users) == len(expected_response)
        assert isinstance(users[0], User)
        assert users == expected_response

    def test__should_return_a_user_that_match_the_given_identifier(
        self,
        user_factory: typing.Callable[..., User],
        user_service_dependencies: typing.Tuple[
            UserService, MemoryUserRepository, LocalNotificationService, LocalIdGenerator
        ]
    ) -> None:
        expected_user = user_factory()
        user_service, user_repository, _, _ = user_service_dependencies
        user_repository.add_multiple([expected_user])

        user = user_service.get_by_id(user_id=expected_user.identifier)

        assert isinstance(user, User)
        assert user == expected_user

    def test__should_raise_a_user_not_found_exception__when_the_user_with_the_given_identifier_does_not_exist(
        self,
        user_service_dependencies: typing.Tuple[
            UserService, MemoryUserRepository, LocalNotificationService, LocalIdGenerator
        ]
    ) -> None:
        wrong_identifier = "any-identifier"
        expected_exception_message = f"The user with the identifier {wrong_identifier} does not exist"
        user_service, user_repository, _, _ = user_service_dependencies

        with pytest.raises(UserNotFound, match=expected_exception_message):
            user_service.get_by_id(user_id=wrong_identifier)

    def test__should_create_a_new_user_when_it_is_called(
        self,
        faker: Faker,
        user_factory: typing.Callable[..., User],
        user_service_dependencies: typing.Tuple[
            UserService, MemoryUserRepository, LocalNotificationService, LocalIdGenerator
        ]
    ) -> None:
        random_identifier = str(faker.uuid4())
        expected_notification_message = "Your account has been created successfully."
        expected_user = user_factory(identifier=random_identifier)
        user_service, user_repository, notification_service, id_generator = user_service_dependencies
        id_generator.set_id_to_generate(identifier=random_identifier)

        response = user_service.create(
            name=expected_user.name,
            lastname=expected_user.lastname,
            email=expected_user.email,
            age=expected_user.age
        )

        assert response == expected_user
        assert user_repository.has_user_been_created(user=expected_user)
        assert notification_service.has_user_been_notified(
            message=expected_notification_message,
            email=expected_user.email
        )

    def test__should_raise_a_user_already_exists_exception__when_the_user_already_exists(
        self,
        user_factory: typing.Callable[..., User],
        user_service_dependencies: typing.Tuple[
          UserService, MemoryUserRepository, LocalNotificationService, LocalIdGenerator
        ]
    ) -> None:
        expected_user = user_factory()
        user_service, user_repository, _, _ = user_service_dependencies
        user_repository.add_multiple([expected_user])
        expected_exception_message = f"The user with the given email already exists"

        with pytest.raises(UserAlreadyExists, match=expected_exception_message):
            user_service.create(
                name=expected_user.name,
                lastname=expected_user.lastname,
                email=expected_user.email,
                age=expected_user.age
            )
