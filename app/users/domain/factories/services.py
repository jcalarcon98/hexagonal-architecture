from app.users.adapters.driven import ConsoleNotificationService
from app.users.domain.ports.driven import NotificationService


def get_notification_service() -> NotificationService:
    return ConsoleNotificationService()
