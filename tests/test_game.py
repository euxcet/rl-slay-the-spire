from rich.console import Console
from rlsts.game.slay_the_spire import SlayTheSpire

class TestGame():
    def test_game(self):
        console = Console()
        game = SlayTheSpire()
        # combat = game.get_act1_easy_combat()
        combat = game.get_act1_boss_combat()
        obs = combat.reset()
        console.log(obs.rich())
        while True:
            action = int(console.input('Input action: '))
            obs = combat.step(action)
            if obs.is_over:
                break
            console.log(obs.rich())
        if obs.is_game_over:
            console.log('You died.')
        else:
            console.log(f'Survied with [bold red]{obs.character_hp}[/bold red] hp')
