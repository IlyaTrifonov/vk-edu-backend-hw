"""
Тесты к Домашнему заданию #1 по Backend Курса Fullstack VK Eduacation.
"""

import pytest

from hw1.main import TicTacToe as Game


class TestCheckWinner:
    """
    Класс для тестирования проверки на победу
    """

    def test_empty_player_data(self):
        """Проверка пустых данных игрока"""
        assert not Game.check_winner([])

    @pytest.mark.parametrize(
        'player_data', [
            [1],
            [3],
            [6],
            [8],
            [5],
        ]
    )
    def test_len_1_player_data(self, player_data):
        """Проверка данных игрока длины 1"""
        assert not Game.check_winner(player_data)

    @pytest.mark.parametrize(
        'player_data', [
            [1, 4],
            [3, 2],
            [6, 7],
            [8, 1],
            [5, 7],
        ]
    )
    def test_len_2_player_data(self, player_data):
        """Проверка данных игрока длины 2"""
        assert not Game.check_winner(player_data)

    @pytest.mark.parametrize(
        'player_data', [
            [8, 7, 6],
            [2, 4, 6],
            [7, 4, 1],
            [3, 4, 5],
            [0, 1, 2],
        ]
    )
    def test_len_3_winning_player_data(self, player_data):
        """Проверка данных игрока длины 3, приводящих к победе"""
        assert Game.check_winner(player_data)

    @pytest.mark.parametrize(
        'player_data', [
            [8, 2, 7],
            [3, 5, 6],
            [3, 5, 2],
            [4, 5, 2],
            [1, 5, 3],
        ]
    )
    def test_len_3_losing_player_data(self, player_data):
        """Проверка данных игрока длины 3, приводящих к проигрышу"""
        assert not Game.check_winner(player_data)

    @pytest.mark.parametrize(
        'player_data', [
            [8, 7, 6, 0],
            [2, 3, 4, 6],
            [7, 0, 4, 1],
            [3, 2, 4, 5],
            [0, 3, 1, 2],
        ]
    )
    def test_len_4_winning_player_data(self, player_data):
        """Проверка данных игрока длины 4, приводящих к победе"""
        assert Game.check_winner(player_data)

    @pytest.mark.parametrize(
        'player_data', [
            [8, 2, 7, 0],
            [3, 1, 6, 4],
            [3, 5, 0, 2],
            [7, 8, 0, 1],
            [0, 5, 6, 4],
        ]
    )
    def test_len_4_losing_player_data(self, player_data):
        """Проверка данных игрока длины 4, приводящих к проигрышу"""
        assert not Game.check_winner(player_data)
