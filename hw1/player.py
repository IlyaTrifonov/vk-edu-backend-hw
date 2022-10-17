"""
Класс пользователя игры в крестики нолики
"""


class Player:
    """
    Класс описывает игрока в Крестики Нолики
    """

    def __init__(self, number: int, sign: str, bot: bool = False):
        self.number = number
        self.sign = sign
        self.player_data = []
        self.bot = bot

    def __str__(self) -> str:
        return f'Игрок {self.number} ({self.sign})'

    def bot_hello(self):
        """Это приветствие игрока бота"""
        if self.bot:
            print(f'Я Игрок-бот {self.number} ({self.sign})')
