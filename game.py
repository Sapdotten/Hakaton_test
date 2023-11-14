"""Файл для реализации логики игры"""
global char
import time
from typing import Union


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
    patterns = ['ppp_p',
                'pppp_',
                'pp_pp',
                'p_ppp',
                '_pppp',
                '_pp_p_',
                '_ppp__',
                '__ppp_',
                '_p_pp_',
                ]

    def __init__(self, field: str):
        global char
        self.char = char
        if char == 'x':
            self.enemy_char = 'o'
        else:
            self.enemy_char = 'x'
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

    def is_danger_pattern(self, char_: str) -> tuple[int, str, str]:

        patterns = []
        for elem in self.patterns:
            patterns.append(elem.replace('p', char_))
        for i in range(0, 19):
            for pattern in patterns:
                ind = self.field[i * 19:i * 19 + 19].find(pattern)
                if ind != -1:
                    return i * 19 + ind, pattern, 'row'
                indw = self.field[i:i + 19 * 18:19].find(pattern)
                if indw != -1:
                    return indw * 19 + i, pattern, 'column'
        for i in range(0, 19):
            for pattern in patterns:
                ind = self.field[i * 19:i - 1:-18].find(pattern)
                ind_d = self.field[342 + i:19 * i + 19:-18].find(pattern)
                ind_lu = self.field[18 - i: 19 + 19 * i:20].find(pattern)
                ind_ld = self.field[19 * i:361 - i:20].find(pattern)
                if ind != -1:
                    return (i - ind) * 19 + ind, pattern, 'diagonal_up'
                if ind_d != -1:
                    return (18 - ind_d) * 19 + i + ind_d, pattern, 'diagonal_up'
                if ind_lu != -1:
                    return ind_lu * 19 + 18 - (i - ind_lu), pattern, 'diagonal_down'
                if ind_ld != -1:
                    return (ind_ld + i) * 19 + ind_ld, pattern, 'diagonal_down'

    def check_neighbors(self, id_: int, type_: str) -> bool:
        """
        Проверяет наличие соседей для выявления Т образного узла
        :param id_: номер ячейки, соседей которой нужно проверить
        :param type_: перпендикулярно оси проверки
        :return: true или false
        """
        if type_ == 'row':
            #         проверяем сверху и снизу
            if self.field[id_ - 19] == self.enemy_char and self.field[id_ + 19] == self.enemy_char:
                return True
            return False
        else:
            if self.field[id_ - 1] == self.enemy_char and self.field[id_ + 1] == self.enemy_char:
                return True
            return False

    def is_T_pattern(self, id_: int, pattern: str, type_: str) -> Union[int, None]:
        pattern = pattern.replace('x', 'p').replace('o', 'p')
        i = 1
        if type_ == 'diagonal_up' or type_ == 'diagonal_down':
            return None
        elif type_ == 'column':
            i = 19
        if (pattern == 'ppp_p' or pattern == '_pp_p_') and self.check_neighbors(id_ + 3*i, type_):
            return id_ + 3 * i
        elif (pattern == 'pppp_' or pattern == '_p_pp_') and self.check_neighbors(id_ + 5*i, type_):
            return id_ + 5*i
        elif (pattern == 'pp_pp' or pattern == '_p_pp_') and self.check_neighbors(id_ + 2*i, type_):
            return id_ + 2*i
        elif pattern == 'p_ppp' and self.check_neighbors(id_ + 1*i, type_):
            return id_ + 1*i
        elif (
                pattern == '_pppp' or pattern == '_pp_p_' or pattern == '_ppp__' or pattern == '_p_pp_') and self.check_neighbors(
            id_, type_):
            return id_
        elif (pattern == '_pp_p_' or pattern == '_ppp__') and self.check_neighbors(id_ + 4*i, type_):
            return id_ + 4*i


char = 'o'
c = "_oo___oo_xoxo__xoo_o_oxx_oo_x______o_______x___oo_x_x_o_x_______oxo___o_x__o_o______x__o_____x__o_____o______x_____xoxoo___xo_____o__x_x__________x__x____o_xo__x__o___x_______o_x______xo______oxo_x_xx__xox___ox____x_oo__ox_x_x___o__________x______________o_____x____o___x___xo___x__x_xo__x_x___ox___x_______x____x_o_x__x_o__ox__o__x__ox_x_____x_oo_____x____o_ox"

a = "_____________x_____"
a += "____________x_x____"
a += "_____________x_____"
a += "_____________x_____"
a += "_____________x_____"
a += "___________________" * 14

f = Field(c)
t1 = time.time()
l = f.is_danger_pattern(f.enemy_char)
print(l)
print(f.is_T_pattern(l[0], l[1], l[2]))
t2 = time.time()
print(t2 - t1)
for i in range(0, 19):
    b = ""
    for elem in c[i * 19:i * 19 + 19]:
        b += f"|{elem}"
    print(b)
