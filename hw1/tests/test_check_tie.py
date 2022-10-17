"""
Тесты к Домашнему заданию #1 по Backend Курса Fullstack VK Eduacation.
"""

import pytest

from hw1.main import TicTacToe as Game


class TestCheckTie:
    """
    Класс для тестирования проверки на ничью
    """

    def test_empty_players_data(self):
        """Проверка пустых данных игроков"""
        assert not Game.check_tie([])

    @pytest.mark.parametrize(
        'players_data', [
            [1, 5, 0, 2],
            [5, 8],
            [4, 6, 3, 0, 1],
            [0, 1, 2, 3, 4, 5, 6, 7],
            [3, 1, 8, 5, 7, 4, 6]
        ]
    )
    def test_players_data_len_smaller_than_9(self, players_data):
        """Проверка данных игроков длины меньше, чем 9"""
        assert not Game.check_tie(players_data)

    @pytest.mark.parametrize(
        'players_data', [
            [2, 1, 4, 8, 0, 5, 7, 3, 6],
            [1, 0, 6, 5, 2, 4, 3, 7, 8],
            [0, 3, 1, 6, 7, 2, 8, 4, 5],
            [0, 1, 2, 3, 4, 5, 6, 7, 8],
            [8, 1, 4, 2, 3, 7, 6, 5, 0]
        ]
    )
    def test_players_data_len_9(self, players_data):
        """Проверка данных игроков длины равной 9"""
        assert Game.check_tie(players_data)
