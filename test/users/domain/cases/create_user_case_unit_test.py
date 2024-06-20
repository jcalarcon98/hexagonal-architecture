import typing

import pytest
from faker import Faker

from app.users.adapters.driven import MemoryUserRepository, LocalNotificationService, LocalIdGenerator
from app.users.domain import User
from app.users.domain.cases import CreateUserCase
from app.users.domain.exceptions import UserAlreadyExists
from app.users.domain.ports.driver import CreateUserUseCase


class TestCreateUserCase:
    @pytest.fixture
    def create_user_case_dependencies(self) -> typing.Tuple[
        CreateUserUseCase,
        MemoryUserRepository,
        LocalNotificationService,
        LocalIdGenerator
    ]:
        memory_user_repository = MemoryUserRepository()
        console_notification_service = LocalNotificationService()
        local_id_generator = LocalIdGenerator()
        create_user_case: CreateUserUseCase = CreateUserCase(
            user_repository=memory_user_repository,
            notification_service=console_notification_service,
            id_generator=local_id_generator
        )
        return create_user_case, memory_user_repository, console_notification_service, local_id_generator

    def test__should_create_a_new_user_when_it_is_called(
        self,
        faker: Faker,
        user_factory: typing.Callable[..., User],
        create_user_case_dependencies: typing.Tuple[
            CreateUserUseCase, MemoryUserRepository, LocalNotificationService, LocalIdGenerator
        ]
    ) -> None:
        random_identifier = str(faker.uuid4())
        expected_notification_message = "Your account has been created successfully."
        expected_user = user_factory(identifier=random_identifier)
        create_user_case, user_repository, notification_service, id_generator = create_user_case_dependencies
        id_generator.set_id_to_generate(identifier=random_identifier)

        response = create_user_case.handle(
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
        create_user_case_dependencies: typing.Tuple[
          CreateUserUseCase, MemoryUserRepository, LocalNotificationService, LocalIdGenerator
        ]
    ) -> None:
        expected_user = user_factory()
        create_user_case, user_repository, _, _ = create_user_case_dependencies
        user_repository.add_multiple([expected_user])
        expected_exception_message = f"The user with the given email already exists"

        with pytest.raises(UserAlreadyExists, match=expected_exception_message):
            create_user_case.handle(
                name=expected_user.name,
                lastname=expected_user.lastname,
                email=expected_user.email,
                age=expected_user.age
            )
