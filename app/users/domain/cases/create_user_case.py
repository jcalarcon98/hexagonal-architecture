from app.domain.ports.driven import IdGenerator, NotificationService
from app.users.domain import User
from app.users.domain.exceptions import UserAlreadyExists
from app.users.domain.ports.driven import UserRepository
from app.users.domain.ports.driver.create_user_use_case import (
    CreateUserUseCase,
    CreateUserUseCaseRequest,
    CreateUserUseCaseResponse
)


class CreateUserCase(CreateUserUseCase):
    def __init__(
        self,
        user_repository: UserRepository,
        notification_service: NotificationService,
        id_generator: IdGenerator
    ):
        self.user_repository = user_repository
        self.notification_service = notification_service
        self.id_generator = id_generator

    def handle(self, request: CreateUserUseCaseRequest) -> CreateUserUseCaseResponse:
        user_attached_to_email = self.user_repository.get_by_email(email=request.email)

        if user_attached_to_email:
            raise UserAlreadyExists(f"The user with the given email already exists")

        new_user = User(
            identifier=self.id_generator.generate(),
            name=request.name,
            lastname=request.lastname,
            email=request.email,
            age=request.age
        )
        user = self.user_repository.create(user=new_user)
        self.notification_service.notify(
            message="Your account has been created successfully.", email=user.email
        )
        return CreateUserUseCaseResponse(user=user)
