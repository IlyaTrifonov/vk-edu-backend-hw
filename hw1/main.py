"""
Домашнее задание #1 по Backend Курса Fullstack VK Eduacation.
"""

import random
import time

from hw1.exceptions import NotACommandException
from hw1.player import Player


class TicTacToe:
    """
    Класс игры в Крестики нолики.
    Обратитесь у объекта к методу start_game(), чтобы начать игру.
    """

    def __init__(self):
        self.board_values = ['-' for _ in range(9)]
        self.rules_is_viewed = False

    @staticmethod
    def show_board(values):
        """Функция для отображения состояния игрового поля"""
        print()
        for i in range(0, 9, 3):
            print(*values[i:i + 3], sep='  ')
        print()

    @staticmethod
    def validate_input(command, valid_comands):
        """
        Функция валидации ввода от пользователя

        Возвращает:
        Саму команду приведённую к типу int, если команда валидная.
        None в случае если команда не валидная.
        """
        try:
            command = int(command)
            if command not in valid_comands:
                raise NotACommandException()
            return command
        except ValueError:
            print('Ошибка! Команда должна быть задана числом!')
            return None
        except NotACommandException as exeption:
            print(exeption.message)
            return None

    @staticmethod
    def game_generation(bot_count: int = 0):
        """
        Функция генерации игроков и права первого хода

        Количество ботов может быть от 0 до 2 включительно.
        В случае введния значения меньше 0, будет выбран 0, больше 2 — 2.
        """
        print('Происходит генерация игры...\n')
        if bot_count > 2:
            bot_count = 2
        if bot_count < 0:
            bot_count = 0
        if random.choice([True, False]):
            player1, player2 = Player(1, 'X'), Player(2, 'O')
        else:
            player1, player2 = Player(1, 'O'), Player(2, 'X')
        print(player1, player2, sep='\n')
        # Активация ботов
        if bot_count:
            print()
        for i in range(bot_count):
            player = [player2, player1][i]
            player.bot = True
            print(f'{player} управляется компьютером.')
        turn = random.randint(1, 2)
        print()
        print(f'Первым ходит {[player1, player2][turn - 1]}')
        return player1, player2, turn

    def game_cycle(self, bot_count: int = 0):
        """Функция запуска одной игры"""
        print()
        player1, player2, turn = self.game_generation(bot_count)
        while True:
            current_player = [player1, player2][turn - 1]
            self.show_board(self.board_values)

            if current_player.bot:
                free_values = [x + 1 for x in range(len(self.board_values))
                               if self.board_values[x] == '-']
                # print(f'Свободные значения {free_values}')
                command = random.choice(free_values)
                print(f'[Bot] {current_player} > ', end='')
                time.sleep(1)
                print(command, end='')
                time.sleep(1)
                print()
            else:
                command = input(f'{current_player} > ')

            # Валидация комманд
            command = self.validate_input(command, [-1] + list(range(1, 10)))
            if not command:
                continue

            if command == -1:
                print(f'\nИгра завершена пользователем {current_player}')
                break
            if command in list(range(1, 10)):
                if self.board_values[command - 1] != '-':
                    print('Ячейка уже занята, выберите другую.')
                    continue
                self.board_values[command - 1] = current_player.sign
                current_player.player_data.append(command - 1)

                # Проверка на победу
                if self.check_winner(current_player.player_data):
                    self.show_board(self.board_values)
                    print(f'Победил {current_player}!')
                    break
                # Проверка на ничью
                if self.check_tie(player1.player_data + player2.player_data):
                    self.show_board(self.board_values)
                    print('Ничья!')
                    break
                turn = 1 if turn == 2 else 2
            else:
                print('Необработанная валидатором ошибка!')  # Ни разу не вылетало
        # Обнуление доски после игры
        self.board_values = ['-' for _ in range(9)]

    def start_game(self):
        """Точка входа в приложение"""
        print('Добро пожаловать в игру «Крестики-нолики»!')
        while True:
            print()
            print('Главное меню:')
            print('1. Начать игру. (два человека)')
            print('2. Начать одиночную игру. (человек и компьютер)')
            print('3. Посмотреть как компьютер сыграет сам с собой.')
            print('4. Правила.')
            print('5. Выйти из игры.')
            command = input('> ')
            if command == '1':
                if not self.rules_is_viewed:
                    self.show_rules()
                self.game_cycle()
            elif command == '2':
                print('Игра с ботом.')
                if not self.rules_is_viewed:
                    self.show_rules()
                self.game_cycle(1)
            elif command == '3':
                self.game_cycle(2)
            elif command == '4':
                self.show_rules()
            elif command == '5':
                break
            else:
                print('Ошибка! Такого варианта в меню нет. Попробуйте ещё раз.')

    @staticmethod
    def check_winner(current_player_data: list):
        """
        Функция для проверки победителя.

        Возвращает:
        True - победил текущий игрок
        False - игра не закончена
        """

        solution = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],
                    [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

        for sol in solution:
            i = 0
            for val in current_player_data:
                if val + 1 in sol:
                    i += 1
                else:
                    continue
            if i == 3:
                return True
        return False

    @staticmethod
    def check_tie(players_data: list):
        """
        Функция для проверки на ничью.

        Возвращает:
        True - ничья, если все ячейки заполнены
        False - игра не закончена
        """
        if len(players_data) == 9:
            return True
        return False

    def show_rules(self):
        """Функция отображает в консоли правила ввода значений для игры в крестики нолики"""
        self.rules_is_viewed = True
        print()
        print('Поговорим немного о правилах:')
        print('Игровое поле представлено в виде сетки 3х3. Каждая ячейка пронумерована.')
        for i in range(1, 9, 3):
            print('  '.join(['-'] * 3), ' ', i, i + 1, i + 2, sep='  ')
        print('Для выбора ячейки необходимо ввести её номер.')
        print('Для выхода из активной игры введите -1')
        print()
        input('Для продолжения нажмите Enter...')


if __name__ == '__main__':
    game = TicTacToe()
    game.start_game()
