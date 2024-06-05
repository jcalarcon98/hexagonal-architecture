from app.users import UserRepository, User
from pytest_mock import MockerFixture


class TestUserRepository:
    def test__get__should_retrieve_all_users__when_it_is_called(self, mocker: MockerFixture) -> None:
        users_info = [
            {
                "id": "012",
                "name": "User",
                "lastName": "Lastname",
                "age": 23,
                "email": "amazing.lastname@gmail.com"
            }
        ]
        mocker.patch("app.users.repository.json.load", return_value=users_info)
        expected_users = [
            User(
                identifier=user_info["id"],
                name=user_info["name"],
                lastname=user_info["lastName"],
                age=user_info["age"],
                email=user_info["email"]
            )
            for user_info in users_info
        ]
        user_repository = UserRepository()

        users = user_repository.get()

        assert isinstance(users, list)
        assert len(users) > 0
        assert isinstance(users[0], User)
        assert users == expected_users

    def test__get_by_id__should_retrieve_the_user_that_match_the_user_id_passed__when_it_is_called(
        self, mocker: MockerFixture
    ) -> None:
        first_user_info = {
            "id": "012",
            "name": "User",
            "lastName": "Lastname",
            "age": 23,
            "email": "amazing.lastname@gmail.com"
        }
        second_user_info = {
            "id": "012",
            "name": "User",
            "lastName": "Lastname",
            "age": 23,
            "email": "amazing.lastname@gmail.com"
        }
        users_info = [first_user_info, second_user_info]
        mocker.patch("app.users.repository.json.load", return_value=users_info)
        expected_user = User(
            identifier=first_user_info["id"],
            name=first_user_info["name"],
            lastname=first_user_info["lastName"],
            age=first_user_info["age"],
            email=first_user_info["email"]
        )
        user_repository = UserRepository()

        user = user_repository.get_by_id(user_id=first_user_info["id"])

        assert isinstance(user, User)
        assert user == expected_user
