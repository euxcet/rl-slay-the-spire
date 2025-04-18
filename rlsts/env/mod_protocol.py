from ..game.combat import Combat, CombatObservation
from ..game.character import Ironclad

class ModProtocol:
    def __init__(self):
        self.for_debug_intent = False

    def to_observation(self, message: dict) -> CombatObservation:
        available_commands = message['available_commands']
        if 'play' not in available_commands:
            return None
        game_state = message['game_state']
        combat_state = game_state['combat_state']
        player = combat_state['player']
        # hand_pile = combat_state['hand']
        # monsters = combat_state['monsters']
        # for monster in monsters:
        #     if monster['intent'] == 'DEBUG':
        #         print('KEY Deck')
        #         key_for_debug = True
        #         return
        # f.write(f"player hp: {player['current_hp']}  block: {player['block']}  energy: {player['energy']}\n")
        
        return CombatObservation(
            is_over=False,
            is_game_over=False,
            character_type=Ironclad,
            character_hp=player['current_hp'],
            character_max_hp=player['max_hp'],
            character_block=player['block'],
            character_energy=player['energy'],
            # for reward
            character_hp_lost=0,
            # TODO

        )
        # return CombatObservation(
        #     is_over=self.is_over,
        #     is_game_over=self.is_game_over,
        #     character_type=type(self.character),
        #     character_hp=self.character.hp,
        #     character_max_hp=self.character.max_hp,
        #     character_block=self.character.block,
        #     character_effects=self.character.effects,
        #     character_energy=self.character.energy,
        #     character_hp_lost=0 if initial_hp is None else initial_hp - self.character.hp,
        #     hand_pile=self.character.hand_pile,
        #     draw_pile=self.character.draw_pile,
        #     discard_pile=self.character.discard_pile,
        #     exhaust_pile=self.character.exhaust_pile,
        #     playing_card=self.character.playing_card,
        #     playing_step=0 if self.character.playing_card is None else self.character.playing_card.step,
        #     enemies_type=[type(enemy) for enemy in self.enemies],
        #     enemies_hp=[enemy.hp for enemy in self.enemies],
        #     enemies_max_hp=[enemy.max_hp for enemy in self.enemies],
        #     enemies_block=[enemy.block for enemy in self.enemies],
        #     enemies_effects=[enemy.effects for enemy in self.enemies],
        #     enemies_intent=[enemy.get_intent() for enemy in self.enemies],
        #     sum_enemies_attack=sum([enemy.get_intent().get_damage() for enemy in self.enemies]),
        #     action_mask=self.get_action_mask(),
        #     error=error,
        # )

    def is_debug_intent(self, message: dict) -> bool:
        if self.for_debug_intent:
            return True
        game_state = message['game_state']
        combat_state = game_state['combat_state']
        monsters = combat_state['monsters']
        for monster in monsters:
            if monster['intent'] == 'DEBUG':
                return True
        return False
    
    def do_debug(self) -> None:
        print('KEY Deck')
        self.for_debug_intent = not self.for_debug_intent