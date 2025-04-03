import json

class TestLog():

    def process_message(self, message) -> None:
        available_commands = message['available_commands']
        ready_for_command = message['ready_for_command']
        if 'play' in available_commands:
            game_state = message['game_state']
            combat_state = game_state['combat_state']
            player = combat_state['player']
            hand_pile = combat_state['hand']
            monsters = combat_state['monsters']
            print(f"player hp: {player['current_hp']}  block: {player['block']}  energy: {player['energy']}")
            for card in hand_pile:
                print(f"\t{card['id']} {card['cost']} upgrades: {card['upgrades']} target: {card['has_target']}")
            for monster in monsters:
                print(f"{monster['id']}[{monster['current_hp']}] intent: {monster['intent']}")
            print()
        elif 'choose' in available_commands:
            try:
                game_state = message['game_state']
                choice_list = game_state['choice_list']
                print('Choices:')
                for choice in choice_list:
                    print(f'\t {choice}')
            except:
                ...


    def test_log(self):
        print()
        # with open('./gamelog/ironclad.txt') as fin:
        with open('./gamelog/debug.txt') as fin:
            lines = fin.readlines()
        for line in lines[:300]:
            if line.startswith('{'):
                message = json.loads(line)
                self.process_message(message)