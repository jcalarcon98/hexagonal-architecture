import typing

from app.users.domain import User
from app.users.domain.exceptions import UserNotFound, UserAlreadyExists
from app.users.domain.ports.driven import UserRepository, NotificationService, IdGenerator
from app.users.domain.ports.driver import UserService


class UserServiceImplementation(UserService):
    def __init__(
        self,
        user_repository: UserRepository,
        notification_service: NotificationService,
        id_generator: IdGenerator
    ):
        self.user_repository = user_repository
        self.notification_service = notification_service
        self.id_generator = id_generator

    def get(self) -> typing.List[User]:
        return self.user_repository.get()

    def get_by_id(self, user_id: str) -> User:
        user = self.user_repository.get_by_id(identifier=user_id)

        if not user:
            raise UserNotFound(f"The user with the identifier {user_id} does not exist")

        return user

    def create(self, name: str, lastname: str, email: str, age: int) -> User:
        user_attached_to_email = self.user_repository.get_by_email(email=email)

        if user_attached_to_email:
            raise UserAlreadyExists(f"The user with the given email already exists")

        new_user = User(
            identifier=self.id_generator.generate(),
            name=name,
            lastname=lastname,
            email=email,
            age=age
        )
        user = self.user_repository.create(user=new_user)
        self.notification_service.notify(
            message="Your account has been created successfully.", email=user.email
        )
        return user
