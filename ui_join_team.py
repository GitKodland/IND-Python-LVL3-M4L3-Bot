from typing import Any

from discord import Interaction
from discord.ui import Button, View

from game_models import Player, Game


class JoinTeamButton(Button):

    def __init__(self, team_number):
        self.team_number = team_number
        super().__init__(label=f"Tim {team_number + 1}")

    async def callback(self, interaction: Interaction) -> Any:
        user = interaction.user
        print(self.team_number)
        await interaction.user.send(f"Kamu bergabung dengan tim {self.team_number + 1}", delete_after=30)
        player = Player(user=interaction.user,
                        game=self.view.game,
                        team_number=self.team_number,
                        info_message=await interaction.user.send("Menghubungkan ke game..."))
        await player.update_info_message(player.questions[0][0][0])
        await self.view.game.update_info_message()

        if not interaction.response.is_done():
            await interaction.response.defer()


class JoinTeamView(View):
    def __init__(self, game: Game):
        super().__init__()
        self.game = game

        for i in range(game.number_of_teams):
            self.add_item(JoinTeamButton(i))
