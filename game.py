"""Файл для реализации логики игры"""

global char


def set_figure(char_: str):
    global char
    char = char_


def get_answer(field: str) -> str:
    """
    Получаем поле в виде строки из 361 символа
    :param field: поле в виде строки из 361 символа
    :return: строку 361 символ
    """
    pass


class Field:
    def __init__(self, field: str):
        global char
        self.char = char
        self.field = field
        # for i in range(0, 19):
        #     self.field.append(field[19 * i:19 * i + 1])

    def ind(self, i: int, j: int):
        return self.field[i * 19 + j]

    def ind(self, i: int, j: int, value: str):
        self.field = self.field[:i * 19 + j] + value + self.field[i * 19 + j + 1:]

    def is_empty(self):
        if self.field == '_' * 361:
            return True

    def first_turn(self):
        self.ind(9, 9, self.char)
