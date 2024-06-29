from app.adapters.driven import ConsoleNotificationService
from app.domain.ports.driven import NotificationService


def get_notification_service() -> NotificationService:
    return ConsoleNotificationService()
