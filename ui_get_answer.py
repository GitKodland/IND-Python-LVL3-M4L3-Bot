from typing import Any

from discord import Interaction
from discord.ui import Button, View, Modal, TextInput


class GetAnswerModal(Modal):
    answer = TextInput(label='')
    def __init__(self, player):
        super().__init__(title='Masukkan jawaban')
        self.player = player

    async def on_submit(self, interaction: Interaction):
        await self.player.handle_answer(self.answer.value)

        if not interaction.response.is_done():
            await interaction.response.defer()


class GetAnswerButton(Button):

    def __init__(self):
        super().__init__(label="Kirim jawaban")

    async def callback(self, interaction: Interaction) -> Any:
        await interaction.response.send_modal(GetAnswerModal(player=self.view.player))

        if not interaction.response.is_done():
            await interaction.response.defer()


class GetAnswerView(View):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.add_item(GetAnswerButton())
