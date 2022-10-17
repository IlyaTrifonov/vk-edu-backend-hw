"""
Тесты к Домашнему заданию #1 по Backend Курса Fullstack VK Eduacation.
"""

import pytest

from hw1.main import TicTacToe as Game


class TestValidateInput:
    """
    Класс для тестирования валидации команд пользователя в процессе игры
    """

    valid_comands = [-1] + list(range(1, 10))

    @pytest.mark.parametrize(
        ('command', 'expected'), [
            ('1', 1),
            ('3', 3),
            ('9', 9),
            ('-1', -1)
        ]
    )
    def test_nums(self, command, expected):
        """Тест для корректного ввода команд"""
        assert Game.validate_input(command, self.valid_comands) == expected

    @pytest.mark.parametrize(
        'command', [
            'datas',
            '2222',
            'python',
            'None',
            'NaN'
        ]
    )
    def test_errors(self, command):
        """
        Тест для ввода ошибочных команд.
        Функция не возвращает ошибок, так как они обрабатываются внутри функции.
        """
        assert Game.validate_input(command, self.valid_comands) is None
