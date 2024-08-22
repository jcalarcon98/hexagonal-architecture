from dataclasses import dataclass


@dataclass
class GetUserBydIdUseCaseRequest:
    identifier: str
