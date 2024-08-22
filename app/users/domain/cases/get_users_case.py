from app.users.domain.ports.driven import UserRepository
from app.users.domain.ports.driver import GetUsersUseCase
from app.users.domain.ports.driver.get_users_use_case import GetUsersUseCaseResponse


class GetUsersCase(GetUsersUseCase):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def handle(self) -> GetUsersUseCaseResponse:
        users = self.user_repository.get()

        return GetUsersUseCaseResponse(users=users)
