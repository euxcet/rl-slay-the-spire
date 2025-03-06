from abc import ABC, abstractmethod

class Enemy(ABC):
    def __init__(
        self,
        hp: int,
    ) -> None:
        ...

    def start_combat(self) -> None:
        ...

    def perform(self) -> None:
        ...
