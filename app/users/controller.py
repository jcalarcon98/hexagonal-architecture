from fastapi import APIRouter

from app.users.adapters import JsonUserRepository
from app.users.ports import UserRepository
from app.users.service import UserService

user_router = APIRouter(prefix="/users")


@user_router.get("/")
def get_users():
    user_repository: UserRepository = JsonUserRepository()
    user_service = UserService(user_repository=user_repository)
    return user_service.get()


@user_router.get("/{user_id}")
def get_user(user_id: str):
    user_repository: UserRepository = JsonUserRepository()
    user_service = UserService(user_repository=user_repository)
    return user_service.get_by_id(user_id=user_id)
