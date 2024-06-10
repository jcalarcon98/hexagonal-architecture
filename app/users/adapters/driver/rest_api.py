from fastapi import APIRouter, Depends, HTTPException

from app.users.adapters import JsonUserRepository
from app.users.domain.exceptions import UserNotFound
from app.users.domain.ports import UserRepository, UserService
from app.users.domain.services import UserServiceImplementation

user_router = APIRouter(prefix="/users")


def get_user_service() -> UserService:
    user_repository: UserRepository = JsonUserRepository()
    user_service: UserService = UserServiceImplementation(user_repository=user_repository)
    return user_service


@user_router.get("/", response_model=None)
def get_users(user_service: UserService = Depends(get_user_service)):
    return user_service.get()


@user_router.get("/{user_id}")
def get_user(user_id: str, user_service: UserService = Depends(get_user_service)):
    try:
        return user_service.get_by_id(user_id=user_id)
    except UserNotFound:
        raise HTTPException(status_code=404)
