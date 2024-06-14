from app.users.domain.ports.driven import NotificationService


class ConsoleNotificationService(NotificationService):
    def notify(self, message: str, email: str) -> None:
        print(f"Sending message: '{message}' to {email}")
