from fastapi import APIRouter, Depends, HTTPException

from app.users.domain import User
from app.users.domain.exceptions import UserNotFound
from app.users.domain.factories import get_users_case, get_user_by_id_case, create_user_case
from app.users.domain.ports.driver import GetUserByIdUseCase, GetUsersUseCase, CreateUserUseCase

from .dtos import User as UserDto
from .outputs import UserOutput

user_router = APIRouter(prefix="/users")


@user_router.get("/", response_model=None)
def get_users(get_users_use_case: GetUsersUseCase = Depends(get_users_case)):
    return get_users_use_case.handle()


@user_router.get("/{user_id}")
def get_user(user_id: str, get_user_by_id_use_case: GetUserByIdUseCase = Depends(get_user_by_id_case)) -> UserOutput:
    try:
        user: User = get_user_by_id_use_case.handle(user_id=user_id)
        return UserOutput(
            identifier=user.identifier,
            name=user.name,
            lastname=user.lastname,
            email=user.email,
            age=user.age
        )
    except UserNotFound:
        raise HTTPException(status_code=404)


@user_router.post("/")
def create_user(user_dto: UserDto, create_user_user_case: CreateUserUseCase = Depends(create_user_case)):
    return create_user_user_case.handle(
        name=user_dto.name,
        lastname=user_dto.lastname,
        email=user_dto.email,
        age=user_dto.age
    )
