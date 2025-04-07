import numpy as np
from ..card import Card

class EventObservation():
    def __init__(
        self,
        event_type: type,
        options: list[bool],
        options_label: list[str],
        character_type: type,
        character_hp: int,
        character_max_hp: int,
        character_gold: int,
        character_deck: list[Card],
        action_mask: np.ndarray,
    ) -> None:
        self.event_type = event_type
        self.options = options
        self.options_label = options_label
        self.character_type = character_type
        self.character_hp = character_hp
        self.character_max_hp = character_max_hp
        self.character_gold = character_gold
        self.character_deck = character_deck
        self.action_mask = action_mask

    def __str__(self) -> str:
        return "EventObservation"

    def rich(self) -> str:
        options_str = ''
        for i, (option, option_label) in enumerate(zip(self.options, self.options_label)):
            options_str += '[bold green]' if option else '[bold red]'
            options_str += f'[{i}][{option_label}]'
            options_str += '[/bold green]' if option else '[/bold red]'
            options_str += '\n'
        character_str = f'[{self.character_type.__name__}] hp: [bold red]{self.character_hp}/{self.character_max_hp}[/bold red] gold: [bold brown]{self.character_gold}[/bold brown]\n'
        return f"Event[[bold yellow]{self.event_type.__name__}[/bold yellow]]\n" + options_str + '\n' + character_str