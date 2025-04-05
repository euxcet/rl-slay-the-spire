from rich.console import Console
from rlsts.game.slay_the_spire import SlayTheSpire
from rlsts.game.card.pile import Pile
from rlsts.game.card.card import CardTargetType

class TestGame():

    def print_pile(self, pile: Pile, label: str, console: Console, offset = 0):
        console.log(label)
        console.log(pile.rich(offset=offset))

    def test_game(self):
        console = Console()
        game = SlayTheSpire()
        # combat = game.get_act1_easy_combat()
        # combat = game.get_act1_boss_combat()
        # combat = game.get_act1_elite_combat()
        combat = game.get_random_combat()
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
