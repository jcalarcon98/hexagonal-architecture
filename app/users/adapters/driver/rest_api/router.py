import typing

from fastapi import APIRouter, Depends

from app.users.domain import User
from app.users.domain.factories import get_users_case, get_user_by_id_case, create_user_case
from app.users.domain.ports.driver import GetUserByIdUseCase, GetUsersUseCase, CreateUserUseCase

from .dtos import UserInput, UserOutput

user_router = APIRouter(prefix="/users")


@user_router.get("/", response_model=typing.List[UserOutput])
def get_users(get_users_use_case: GetUsersUseCase = Depends(get_users_case)):
    users = get_users_use_case.handle()
    return [
        UserOutput(
            identifier=user.identifier,
            name=user.name,
            lastname=user.lastname,
            email=user.email,
            age=user.age
        )
        for user in users
    ]


@user_router.get("/{user_id}")
def get_user(user_id: str, get_user_by_id_use_case: GetUserByIdUseCase = Depends(get_user_by_id_case)) -> UserOutput:
    user: User = get_user_by_id_use_case.handle(user_id=user_id)
    return UserOutput(
        identifier=user.identifier,
        name=user.name,
        lastname=user.lastname,
        email=user.email,
        age=user.age
    )


@user_router.post("/", response_model=UserOutput)
def create_user(
    user_dto: UserInput, create_user_user_case: CreateUserUseCase = Depends(create_user_case)
) -> UserOutput:
    user = create_user_user_case.handle(
        name=user_dto.name,
        lastname=user_dto.lastname,
        email=user_dto.email,
        age=user_dto.age
    )
    return UserOutput(
        identifier=user.identifier,
        name=user.name,
        lastname=user.lastname,
        email=user.email,
        age=user.age
    )
