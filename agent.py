import os
import json
import sys
import time

root = '/Users/euxcet/Project/rl-slay-the-spire/gamelog'
fname = 'ironclad'

f = open(os.path.join(root, fname + '.txt'), 'w')
print('Ready')

flog = open(os.path.join(root, 'log.txt'), 'w')
flog.write(sys.version + ' ' + sys.executable + '\n')

key_for_debug = False

def process_message(message) -> None:
    global f, key_for_debug
    if key_for_debug:
        print('KEY Deck')
        key_for_debug = False
        return
    available_commands = message['available_commands']
    ready_for_command = message['ready_for_command']
    if 'play' in available_commands:
        game_state = message['game_state']
        combat_state = game_state['combat_state']
        player = combat_state['player']
        hand_pile = combat_state['hand']
        monsters = combat_state['monsters']
        for monster in monsters:
            if monster['intent'] == 'DEBUG':
                print('KEY Deck')
                key_for_debug = True
                return
        f.write(f"player hp: {player['current_hp']}  block: {player['block']}  energy: {player['energy']}\n")
        for card in hand_pile:
            f.write(f"\t{card['id']} {card['cost']} upgrades: {card['upgrades']}\n")
        for monster in monsters:
            f.write(f"{monster['id']}[{monster['current_hp']}] intent: {monster['intent']}\n")
        f.write('\n')
        f.flush()
    elif 'choose' in available_commands:
        try:
            game_state = message['game_state']
            choice_list = game_state['choice_list']
            f.write('Choices:\n')
            for choice in choice_list:
                f.write(f'\t {choice}\n')
            f.flush()
        except:
            ...

while True:
    x = input()
    data: dict = json.loads(x)

    process_message(data)

    flog.write(x)
    flog.write('\n')
    flog.flush()
    if data.get('error') is not None and len(data.get('error')) > 0:
        continue
