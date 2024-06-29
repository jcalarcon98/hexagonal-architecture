from app.users.domain.cases import GetUserByIdCase, GetUsersCase, CreateUserCase
from app.users.domain.ports.driver import GetUserByIdUseCase, GetUsersUseCase, CreateUserUseCase
from app.domain.ports.driven import NotificationService, IdGenerator
from .repositories import get_user_repository
from .services import get_notification_service
from .generators import get_id_generator


def get_user_by_id_case() -> GetUserByIdUseCase:
    user_repository_instance = get_user_repository()
    get_user_by_id_case_instance = GetUserByIdCase(
        user_repository=user_repository_instance
    )
    return get_user_by_id_case_instance


def get_users_case() -> GetUsersUseCase:
    user_repository_instance = get_user_repository()
    get_users_case_instance = GetUsersCase(
        user_repository=user_repository_instance
    )
    return get_users_case_instance


def create_user_case() -> CreateUserUseCase:
    user_repository_instance = get_user_repository()
    notification_service: NotificationService = get_notification_service()
    id_generator: IdGenerator = get_id_generator()
    create_user_case_instance = CreateUserCase(
        user_repository=user_repository_instance,
        notification_service=notification_service,
        id_generator=id_generator
    )
    return create_user_case_instance
