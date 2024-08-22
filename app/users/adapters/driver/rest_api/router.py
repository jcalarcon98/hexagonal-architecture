import typing

from fastapi import APIRouter, Depends

from app.users.domain import User
from app.users.domain.factories import get_users_case, get_user_by_id_case, create_user_case
from app.users.domain.ports.driver import GetUserByIdUseCase, GetUsersUseCase, CreateUserUseCase
from app.users.domain.ports.driver.create_user_use_case import CreateUserUseCaseRequest
from app.users.domain.ports.driver.get_user_by_id_use_case import GetUserBydIdUseCaseRequest

from .dtos import UserInput, UserOutput

user_router = APIRouter(prefix="/users")


@user_router.get("/", response_model=typing.List[UserOutput])
def get_users(get_users_use_case: GetUsersUseCase = Depends(get_users_case)):
    get_users_use_case_response = get_users_use_case.handle()
    users = get_users_use_case_response.users
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


@user_router.get("/{user_id}", response_model=UserOutput)
def get_user(user_id: str, get_user_by_id_use_case: GetUserByIdUseCase = Depends(get_user_by_id_case)) -> UserOutput:
    get_user_by_id_use_case_request = GetUserBydIdUseCaseRequest(
        identifier=user_id
    )
    get_user_by_id_use_case_response = get_user_by_id_use_case.handle(request=get_user_by_id_use_case_request)
    user = get_user_by_id_use_case_response.user
    return UserOutput(
        identifier=user.identifier,
        name=user.name,
        lastname=user.lastname,
        email=user.email,
        age=user.age
    )


@user_router.post("/", response_model=UserOutput)
def create_user(
    user_input: UserInput, create_user_use_case: CreateUserUseCase = Depends(create_user_case)
) -> UserOutput:
    create_user_use_case_request = CreateUserUseCaseRequest(
        name=user_input.name,
        lastname=user_input.lastname,
        email=user_input.email,
        age=user_input.age
    )
    create_user_use_case_response = create_user_use_case.handle(request=create_user_use_case_request)
    user = create_user_use_case_response.user
    return UserOutput(
        identifier=user.identifier,
        name=user.name,
        lastname=user.lastname,
        email=user.email,
        age=user.age
    )
