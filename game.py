"""Файл для реализации логики игры"""
global char
import time


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
                indw = self.field[i:i + 19:19].find(pattern)
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


char = 'o'
c = "_oo___oo_xoxo__xoo_o_oxx_oo_x______o_______x___oo_x_x_o_x_______oxo___o_x__o_o______x__o_____x__o_____o______x_____xoxoo___xo_____o__x_x__________x__x____o_xo__x__o___x_______o_x______xo______oxo_x_xx__xox___ox____x_oo__ox_x_x___o__________x______________o_____x____o___x___xo___x__x_xo__x_x___ox___x_______x____x_o_x__x_o__ox__o__x__ox_x_____x_oo_____x____o_ox"

a = "_____________x_____"
a += "______________x____"
a += "_______________x___"
a += "___________________"
a += "_________________x_"
a += "___________________" * 14

f = Field(c)
t1 = time.time()
print(f.is_danger_pattern())
t2 = time.time()
print(t2 - t1)
for i in range(0, 19):
    b = ""
    for elem in c[i * 19:i * 19 + 19]:
        b += f"|{elem}"
    print(b)
