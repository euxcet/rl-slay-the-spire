import numpy as np
from ..effect.effect import Effect
from ..enemy.intent import Intent
from ..card import Card, Pile

class CombatObservation():
    def __init__(
        self,
        is_over: bool,
        is_game_over: bool,
        character_type: type,
        character_hp: int,
        character_max_hp: int,
        character_block: int,
        character_energy: int,
        character_effects: list[Effect],
        character_hp_lost: int,
        hand_pile: Pile,
        draw_pile: Pile,
        discard_pile: Pile,
        exhaust_pile: Pile,
        playing_card: Card | None,
        playing_step: int,
        enemies_type: list[type],
        enemies_hp: list[int],
        enemies_max_hp: list[int],
        enemies_block: list[int],
        enemies_effects: list[list[Effect]],
        enemies_intent: list[Intent],
        sum_enemies_attack: int,
        action_mask: np.ndarray,
        error: str,
    ) -> None:
        self.is_over = is_over
        self.is_game_over = is_game_over
        self.character_type = character_type
        self.character_hp = character_hp
        self.character_max_hp = character_max_hp
        self.character_block = character_block
        self.character_effects = character_effects
        self.character_energy = character_energy
        self.character_hp_lost = character_hp_lost
        self.hand_pile = hand_pile
        self.draw_pile  = draw_pile
        self.discard_pile = discard_pile
        self.exhaust_pile = exhaust_pile
        self.playing_card = playing_card
        self.playing_step = playing_step
        self.enemies_type = enemies_type
        self.enemies_hp = enemies_hp
        self.enemies_max_hp = enemies_max_hp
        self.enemies_block = enemies_block
        self.enemies_effects = enemies_effects
        self.enemies_intent = enemies_intent
        self.sum_enemies_attack = sum_enemies_attack
        self.action_mask = action_mask
        self.error = error

    def __str__(self) -> str:
        # TODO
        enemies_str = '\n'.join(
            [
                f'{type.__name__}\n' + \
                f'hp: {hp} block:{block}\n' + \
                f'effects: {effects}\n' + \
                f'intent: {intent}'
                for type, hp, block, effects, intent in
                    zip(self.enemies_type, self.enemies_hp, self.enemies_block, self.enemies_effects, self.enemies_intent)
            ]
        )
        return f'\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n' + \
               f'{self.character_type.__name__}\n' + \
               f'hp: {self.character_hp} block: {self.character_block}\n' + \
               f'effects: {self.character_effects}\n\n' + \
               enemies_str + '\n' + \
               f'<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n'

    def __repr__(self) -> str:
        return self.__str__()

    def format_effect(self, effects: list[Effect]) -> str:
        e = ' '.join([type(effect).__name__ + f'[{effect.stack}]' for effect in effects])
        return f'effects: {e}\n'

    def rich(self) -> str:
        enemies_str = '\n'.join(
            [
                f'[white underline]{type.__name__}[{id}][/white underline]\n' + \
                f'hp: [bold red]{hp}[/bold red] block: [bold green]{block}[/bold green]\n' + \
                self.format_effect(effects) + \
                f'intent: {intent.rich()}'
                for id, (type, hp, block, effects, intent) in
                    enumerate(zip(self.enemies_type, self.enemies_hp, self.enemies_block, self.enemies_effects, self.enemies_intent))
            ]
        )
        cards_str = ' '.join([f'[bold green]{type(card).__name__}[{id + 1}][/bold green]' for id, card in enumerate(self.hand_pile.cards)]) + '\n'
        playing_card = 'None' if self.playing_card is None else f'[bold yellow]{type(self.playing_card).__name__}[/bold yellow] {self.playing_step}'
        return f'\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n' + \
               f'[bold blue]{self.character_type.__name__}[/bold blue]\n' + \
               f'hp: [bold red]{self.character_hp}[/bold red] block: [bold green]{self.character_block}[/bold green] energy: [bold yellow]{self.character_energy}[/bold yellow]\n' + \
               self.format_effect(self.character_effects) + \
               f'cards: {cards_str}' + \
               f'playing: {playing_card}' + \
               f'\n\n' + \
               enemies_str + '\n' + \
               f'<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n'
