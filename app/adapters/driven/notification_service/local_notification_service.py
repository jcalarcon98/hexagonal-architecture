import typing

from app.domain.ports.driven import NotificationService


class LocalNotificationService(NotificationService):

    def __init__(self):
        self.users_notified: typing.Dict[str, str] = {}

    def notify(self, message: str, email: str) -> None:
        self.users_notified = {email: message}
        print(f"Sending notification '{message}' to user {email}")

    def has_user_been_notified(self, message: str, email: str) -> bool:
        user_message = self.users_notified.get(email)

        if not user_message:
            return False

        return user_message == message
