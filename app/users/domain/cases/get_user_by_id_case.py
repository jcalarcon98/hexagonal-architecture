from app.users.domain import User
from app.users.domain.exceptions import UserNotFound
from app.users.domain.ports.driven import UserRepository
from app.users.domain.ports.driver.get_user_by_id_use_case import (
    GetUserByIdUseCase,
    GetUserBydIdUseCaseRequest,
    GetUserBydIdUseCaseResponse
)


class GetUserByIdCase(GetUserByIdUseCase):

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def handle(self, request: GetUserBydIdUseCaseRequest) -> GetUserBydIdUseCaseResponse:
        user = self.user_repository.get_by_id(identifier=request.identifier)

        if not user:
            raise UserNotFound(f"The user with the identifier {request.identifier} does not exist")

        return GetUserBydIdUseCaseResponse(user=user)
