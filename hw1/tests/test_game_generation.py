"""
Тесты к Домашнему заданию #1 по Backend Курса Fullstack VK Eduacation.
"""

import pytest

from hw1.main import TicTacToe as Game
from hw1.player import Player


class TestGameGeneration:
    """
    Класс для тестирования генератора игры.
    """

    def test_types(self):
        """Тест на проверку типа возвращаемых значений функции"""
        player1, player2, turn = Game.game_generation()
        p1_check = isinstance(player1, Player)
        p2_check = isinstance(player2, Player)
        turn_check = isinstance(turn, int)
        assert p1_check and p2_check and turn_check


    #Вспомним правило: «Явное лучше, чем неявное»

    def test_bot_none(self):
        """Проверка количества ботов при вызове без параметров"""
        player1, player2, _ = Game.game_generation()
        assert player1.bot == False and player2.bot == False

    def test_bot_0(self):
        """Проверка количества ботов при вызове с параметром 0"""
        player1, player2, _ = Game.game_generation(0)
        assert player1.bot == False and player2.bot == False

    def test_bot_1(self):
        """Проверка количества ботов при вызове с параметром 1"""
        player1, player2, _ = Game.game_generation(1)
        assert player1.bot == False and player2.bot == True

    def test_bot_2(self):
        """Проверка количества ботов при вызове с параметром 2"""
        player1, player2, _ = Game.game_generation(2)
        assert player1.bot == True and player2.bot == True

    @pytest.mark.parametrize(
        'bot_count', [
            -1, -10, -100
        ]
    )
    def test_bot_smaller_than_0(self, bot_count):
        """Проверка количества ботов при вызове с параметром меньше 0"""
        player1, player2, _ = Game.game_generation(bot_count)
        assert player1.bot == False and player2.bot == False

    @pytest.mark.parametrize(
        'bot_count', [
            3, 8, 100, 999
        ]
    )
    def test_bot_more_than_2(self, bot_count):
        """Проверка количества ботов при вызове с параметром больше 2"""
        player1, player2, _ = Game.game_generation(bot_count)
        assert player1.bot == True and player2.bot == True

    def test_bot_is_str(self):
        """Проверка возвращаемого значения при вызове с параметром типа str"""
        with pytest.raises(TypeError):
            Game.game_generation('sda')

    def test_bot_is_float(self):
        """Проверка возвращаемого значения при вызове с параметром типа float"""
        with pytest.raises(TypeError):
            Game.game_generation(1.3)
