from ..effect.effect import Effect

class CombatObservation():
    def __init__(
        self,
        character_hp: int,
        character_block: int,
        character_status: list[Effect],
        enemies_hp: list[int],
        enemies_block: list[int],
        enemies_effect: list[list[Effect]],
        # enemies_intent: list[list[Intent]],
        sum_enemies_attack: int,
    ) -> None:
        self.character_hp = character_hp
        self.character_block = character_block
        self.character_status = character_status
        self.enemies_hp = enemies_hp
        self.enemies_block = enemies_block
        self.enemies_effect = enemies_effect
        self.sum_enemies_attack = sum_enemies_attack