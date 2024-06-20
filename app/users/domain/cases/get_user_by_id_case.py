from app.users.domain import User
from app.users.domain.exceptions import UserNotFound
from app.users.domain.ports.driven import UserRepository
from app.users.domain.ports.driver import GetUserByIdUseCase


class GetUserByIdCase(GetUserByIdUseCase):

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def handle(self, user_id: str) -> User:
        user = self.user_repository.get_by_id(identifier=user_id)

        if not user:
            raise UserNotFound(f"The user with the identifier {user_id} does not exist")

        return user
