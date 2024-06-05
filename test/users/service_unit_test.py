from app.users import UserService, User
from pytest_mock import MockerFixture


class TestUserService:
    def test__get__should_return_a_list_of_users(self, mocker: MockerFixture) -> None:
        expected_users = [
            User(
                identifier="123",
                name="Jean",
                lastname="Alarcon",
                age=26,
                email="jean.alarcon@gmail.com"
            )
        ]
        mocker.patch(
            target="app.users.service.UserRepository",
            return_value=mocker.Mock(
                get=mocker.Mock(
                    return_value=expected_users
                )
            )
        )
        user_service = UserService()

        users = user_service.get()

        assert isinstance(users, list)
        assert users == expected_users

    def test__get_by_id__should_return_a_user(self, mocker: MockerFixture) -> None:
        expected_user = User(
            identifier="123",
            name="Jean",
            lastname="Alarcon",
            age=26,
            email="jean.alarcon@gmail.com"
        )
        mocker.patch(
            target="app.users.service.UserRepository",
            return_value=mocker.Mock(
                get_by_id=mocker.Mock(
                    return_value=expected_user
                )
            )
        )
        user_service = UserService()

        user = user_service.get_by_id(user_id=expected_user.identifier)

        assert isinstance(user, User)
        assert user == expected_user
