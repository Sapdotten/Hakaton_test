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
    patterns = ['ppp_ppp',
                'ppp_p',
                'pp_pp',
                'p_ppp',
                'pppp_',
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

    def make_turn(self) -> str:
        if self.is_empty():
            self.first_turn()
            return self.field
        data = self.is_danger_pattern(self.enemy_char)
        if data is not None:
            p_ind = data[0]
            pattern = data[1]
            type_ = data[2]
            t_ind = self.is_T_pattern(p_ind, pattern, type_, self.enemy_char)
            if t_ind is not None:
                self.set_value(t_ind, self.char)
                return self.field
            else:
                ind = self.get_block_ind(p_ind, pattern, type_)
                self.set_value(ind, self.char)
                return self.field

    def get_block_ind(self, ind_: int, pattern: str, type_: str) -> int:
        pattern = pattern.replace('o', 'p').replace('x', 'p')
        i = get_offset(type_)
        if pattern == 'ppp_ppp' or pattern == 'ppp_p' or pattern == '_pp_p_':
            return ind_ + 3 * i
        elif pattern == 'pp_pp' or pattern == '_p_pp_':
            return ind_ + i * 2
        elif pattern == 'p_ppp':
            return ind_ + i
        elif pattern == 'pppp_':
            return ind_ + i * 4
        elif pattern == '_pppp':
            return ind_
        elif pattern == '_ppp__':
            return self.get_most_closer_place([ind_,
                                               ind_ + i * 4])
        elif pattern == '__ppp_':
            return self.get_most_closer_place([ind_ + i,
                                               ind_ + i * 5])

    def ind(self, i: int, j: int):
        return self.field[i * 19 + j]

    def ind(self, i: int, j: int, value: str):
        self.field = self.field[:i * 19 + j] + value + self.field[i * 19 + j + 1:]

    def set_value(self, ind_: int, value: str):
        self.field = self.field[:ind_] + value + self.field[ind_ + 1:]

    def is_empty(self):
        if self.field == '_' * 361:
            return True
        return False

    def first_turn(self):
        self.ind(9, 9, self.char)

    def is_our_on_field(self):
        if self.char in self.field:
            return True
        return False

    def get_coords(self, ind_: int) -> tuple[int, int]:
        col = ind_ % 19
        row = ind_ // 19
        return row, col

    def second_turn(self):
        ind_ = self.field.find(self.enemy_char)

    def get_count(self, id_: int, offsets: list) -> int:
        count = 0
        for offset in offsets:
            if self.field[id_ + offset] == self.char:
                count += 1
            elif self.field[id_ + offset] == self.enemy_char:
                count -= 1
        return count

    def get_most_closer_place(self, ids: list) -> int:
        offsets = [-20, -19, -18, 1, 20, 19, 18, -1]
        max_count = -9
        max_id = 0
        for id_ in ids:
            count = 0
            if not is_on_borderline(id_):
                count = self.get_count(id_, offsets)
                if count > max_count:
                    max_count = count
                    max_id = id_
            else:
                if id_ == 0:
                    count = self.get_count(id_, offsets[3:6])
                elif id_ == 18:
                    count = self.get_count(id_, offsets[5:8])
                elif id_ == 342:
                    count = self.get_count(id_, offsets[1:4])
                elif id_ == 360:
                    count = self.get_count(id_, offsets[0:2] + offsets[7:9])
                if 0 < id_ < 18:
                    count = self.get_count(id_, offsets[3:8])
                elif (id_ + 1) % 19 == 0:
                    count = self.get_count(id_, offsets[0:2] + offsets[5:9])
                elif (id_ + 1) % 19 == 1:
                    count = self.get_count(id_, offsets[1:6])
                else:
                    count = self.get_count(id_, offsets[0:4] + offsets[7:9])
                if count > max_count:
                    max_count = count
                    max_id = id_
        return max_id

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

    def check_neighbors(self, id_: int, type_: str, char_: str) -> bool:
        """
        Проверяет наличие соседей для выявления Т образного узла
        :param id_: номер ячейки, соседей которой нужно проверить
        :param type_: перпендикулярно оси проверки
        :param char_: символ, который ищем у соседей
        :return: true или false
        """
        if is_on_borderline(id_):
            return False
        i = 1
        if type_ == 'row':
            i = 19
        elif type_ == 'diagonal_up':
            i = 20
        elif type_ == 'diagonal_down':
            i = 18
        if self.field[id_ - i] == char_ and self.field[id_ + i] == char_:
            return True
        return False

    def is_T_pattern(self, id_: int, pattern: str, type_: str, char_: str) -> Union[int, None]:
        """Возвращает номер символа, в котором можно предупредить T образный паттерн"""

        pattern = pattern.replace('x', 'p').replace('o', 'p')
        i = get_offset(type_)
        if (pattern == 'ppp_p' or pattern == '_pp_p_' or pattern == 'ppp_ppp') and self.check_neighbors(id_ + 3 * i,
                                                                                                        type_, char_):
            return id_ + 3 * i
        elif (pattern == 'pppp_' or pattern == '_p_pp_') and self.check_neighbors(id_ + 5 * i, type_, char_):
            return id_ + 5 * i
        elif (pattern == 'pp_pp' or pattern == '_p_pp_') and self.check_neighbors(id_ + 2 * i, type_, char_):
            return id_ + 2 * i
        elif pattern == 'p_ppp' and self.check_neighbors(id_ + 1 * i, type_, char_):
            return id_ + 1 * i
        elif (
                pattern == '_pppp' or pattern == '_pp_p_' or pattern == '_ppp__' or pattern == '_p_pp_') and self.check_neighbors(
            id_, type_, char_):
            return id_
        elif (pattern == '_ppp__') and self.check_neighbors(id_ + 4 * i,
                                                            type_, char_):
            return id_ + 4 * i


def is_on_borderline(id_: int):
    if (id_ + 1) % 19 == 0 or (id_ + 1) % 19 == 1 or (0 <= id_ <= 18) or (342 <= id_ <= 360):
        return True
    return False


def get_offset(type_: str) -> int:
    i = 1
    if type_ == 'column':
        i = 19
    elif type_ == 'diagonal_up':
        i = 18
    elif type_ == 'diagonal_down':
        i = 20
    return i


char = 'o'
c = "_oo___oo_xoxo__xoo_o_oxx_oo_x______o_______x___oo_x_x_o_x_______oxo___o_x__o_o______x__o_____x__o_____o______x_____xoxoo___xo_____o__x_x__________x__x____o_xo__x__o___x_______o_x______xo______oxo_x_xx__xox___ox____x_oo__ox_x_x___o__________x______________o_____x____o___x___xo___x__x_xo__x_x___ox___x_______x____x_o_x__x_o__ox__o__x__ox_x_____x_oo_____x____o_ox"

a = "_________________x_"
a += "________________x_x"
a += "_________________x_"
a += "_________________x_"
a += "_________________x_"
a += "___________________" * 14

f = Field(c)
t1 = time.time()
# l = f.is_danger_pattern(f.enemy_char)
# print(l)
# print(f.is_T_pattern(l[0], l[1], l[2], f.enemy_char))
# print(f.get_most_closer_place([l[0] + 2]))

for i in range(0, 19):
    b = ""
    for elem in c[i * 19:i * 19 + 19]:
        b += f"|{elem}"
    print(b)
c = f.make_turn()
print("Making a move: ")
for i in range(0, 19):
    b = ""
    for elem in c[i * 19:i * 19 + 19]:
        b += f"|{elem}"
    print(b)
t2 = time.time()
print(t2 - t1)
