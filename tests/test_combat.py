from rich.console import Console
from rlsts.game.character import Ironclad
from rlsts.game.combat import Combat, random_combat
from rlsts.game.card.deck import Deck
from rlsts.game.card.pile import Pile
from rlsts.game.card.card import CardTargetType

class TestCombat():

    def print_pile(self, pile: Pile, label: str, console: Console, offset = 0):
        console.log(label)
        console.log(pile.rich(offset=offset))

    def test_combat(self):
        console = Console()
        combat = random_combat(Ironclad(deck=Deck.ironclad_random_deck()))
        obs = combat.reset()
        console.log(obs.rich())
        while True:
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
                action = int(command)
            except ValueError as e:
                continue
            obs = combat.step(action)
            if obs.is_over:
                break
            console.log(obs.rich())

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
        else:
            console.log(f'Survied with [bold red]{obs.character_hp}[/bold red] hp')
