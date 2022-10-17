"""
Файл с описанием кастомных ошибок для игры Крестики Нолики
"""


class NotACommandException(Exception):
    """Ошибка недопустимой команды"""

    def __init__(self, message='Ошибка! Введена недопустимая команда!') -> None:
        self.message = message
