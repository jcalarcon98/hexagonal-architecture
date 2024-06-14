import typing

from fastapi import APIRouter, Depends, HTTPException

from app.users.adapters.driven import MemoryUserRepository, ConsoleNotificationService, RandomIdGenerator
from app.users.domain.exceptions import UserNotFound
from app.users.domain.ports.driven import UserRepository, NotificationService, IdGenerator
from app.users.domain.ports.driver import UserService
from app.users.domain.services import UserServiceImplementation

from .dtos import User as UserDto

user_router = APIRouter(prefix="/users")


user_service_instance: typing.Optional[UserService] = None


def get_user_service() -> UserService:
    global user_service_instance
    if not user_service_instance:
        user_repository: UserRepository = MemoryUserRepository()
        notification_service: NotificationService = ConsoleNotificationService()
        id_generator: IdGenerator = RandomIdGenerator()
        user_service_instance = UserServiceImplementation(
            user_repository=user_repository,
            notification_service=notification_service,
            id_generator=id_generator
        )
    return user_service_instance


@user_router.get("/", response_model=None)
def get_users(user_service: UserService = Depends(get_user_service)):
    return user_service.get()


@user_router.get("/{user_id}")
def get_user(user_id: str, user_service: UserService = Depends(get_user_service)):
    try:
        return user_service.get_by_id(user_id=user_id)
    except UserNotFound:
        raise HTTPException(status_code=404)


@user_router.post("/")
def create_user(user_dto: UserDto, user_service: UserService = Depends(get_user_service)):
    return user_service.create(
        name=user_dto.name,
        lastname=user_dto.lastname,
        email=user_dto.email,
        age=user_dto.age
    )
