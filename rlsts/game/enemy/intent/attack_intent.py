from .intent import Intent
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...enemy import Enemy

class AttackIntent(Intent):
    def __init__(self, enemy: 'Enemy', values: list[int], is_multi: bool = True) -> None:
        super().__init__(enemy=enemy, values=values)
        if is_multi:
            assert(len(self.values) >= 2)
        else:
            assert(len(self.values) >= 1)
        self.is_multi = is_multi
        self.values = values

    def is_attack(self) -> bool:
        return True

    def get_damage(self) -> int:
        if self.is_multi:
            return self.enemy.estimate_attack(self.values[0]) * self.values[1]
        else:
            return self.enemy.estimate_attack(self.values[0])

    def perform(self) -> None:
        if self.is_multi:
            for _ in range(self.values[1]):
                self.enemy.attack(self.values[0])
        else:
            self.enemy.attack(self.values[0])

    def other_values_str(self) -> str:
        if self.is_multi:
            return f"[{' '.join(map(str, self.values[2:]))}]"
        else:
            return f"[{' '.join(map(str, self.values[1:]))}]"

    def __str__(self) -> str:
        attack = self.enemy.estimate_attack(self.values[0])
        if self.is_multi:
            return f"{type(self).__name__} {attack} * {self.values[1]} = {attack * self.values[1]} {self.other_values_str()}"
        else:
            return f"{type(self).__name__} {attack} * 1 = {attack} {self.other_values_str()}"

    def rich(self) -> str:
        attack = self.enemy.estimate_attack(self.values[0])
        if self.is_multi:
            return f"{type(self).__name__} {attack} * {self.values[1]} = [bold red]{attack * self.values[1]}[/bold red] {self.other_values_str()}"
        else:
            return f"{type(self).__name__} {attack} * 1 = [bold red]{attack}[/bold red] {self.other_values_str()}"