class User:
    def __init__(self, identifier: str, name: str, lastname: str, age: int, email: str):
        self.identifier = identifier
        self.name = name
        self.lastname = lastname
        self.age = age
        self.email = email

    def __eq__(self, other: "User") -> bool:
        if not isinstance(other, User):
            return False
        return (
            self.identifier == other.identifier and
            self.name == other.name and
            self.lastname == other.lastname and
            self.age == other.age and
            self.email == other.email
        )
