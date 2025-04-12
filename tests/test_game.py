from rich.console import Console
from rlsts.game.character import Ironclad
from rlsts.game.combat import Combat, random_combat
from rlsts.game.slay_the_spire import SlayTheSpire
from rlsts.game.card.deck import Deck
from rlsts.game.card.pile import Pile
from rlsts.game.card.card import CardTargetType
from rlsts.game.observation import CombatObservation
from rlsts.game.observation import ChooseRoomObservation

class TestGame():

    def print_pile(self, pile: Pile, label: str, console: Console, offset = 0):
        console.log(label)
        console.log(pile.rich(offset=offset))

    def test_game(self):
        console = Console()
        console.log()
        game = SlayTheSpire()
        obs = game.reset()
        while True:
            console.log('\n' + obs.rich())
            try:
                command = console.input('Input action: ')
                if command == 'q':
                    self.print_pile(obs.draw_pile, 'Draw Pile', console, offset=0)
                    continue
                elif command == 'w':
                    self.print_pile(obs.discard_pile, 'Discard Pile', console, offset=0)
                    continue
                elif command == 'e':
                    self.print_pile(obs.exhaust_pile, 'Exhaust Pile', console, offset=0)
                    continue
                elif command == 'r':
                    self.print_pile(obs.hand_pile, 'Hand Pile', console, offset=1)
                    continue
                elif command == 'd':
                    self.print_pile(Pile(cards=game.character.deck.cards), 'Deck', console, offset=0)
                    continue
                action = int(command)
            except ValueError as e:
                continue

            if action >= len(obs.action_mask) or obs.action_mask[action] == 0:
                continue
            obs = game.step(action)
            if isinstance(obs, CombatObservation):
                if obs.playing_card:
                    console.log('[bold]Choice list:[/bold]')
                    choices = obs.playing_card.get_choice_list()
                    console.log(
                        " ".join([
                            choice[0].rich(i, style=['bold red', 'bold green'][int(choice[1])])
                            for i, choice in enumerate(choices)
                        ])
                    )
                if obs.is_game_over:
                    console.log('You died.')
                    break
            if isinstance(obs, ChooseRoomObservation):
                if obs.is_win:
                    console.log('You win.')
                    break

