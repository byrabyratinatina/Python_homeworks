#Без PIP
#print('*'*100)
#print('\n')
#print('А давайте играть в крестики-нолики!')

#board = list(range(1,10))

# def design_board(board):
#     print('-'*12)
#     for i in range(3):
#         print('|', board[0+i*3],'|', board[1+i*3], '|', board[2+i*3], '|')
#         print('-'*12)

# # design_board(board)

# def choice(tic_tac):
#     valid = False
#     while not valid:
#         player_index = input('Ваш ход, выберите ячейку ' + tic_tac + ' --> ')
#         try:
#             player_index =int(player_index)
#         except:
#             print('Что то не то нажали')
#             continue
#         if player_index >= 1 and player_index <= 9:
#             if(str(board[player_index-1]) not in 'XO'):
#                 board[player_index-1] = tic_tac
#                 valid = True
#             else:
#                 print('Занято')
#         else:
#             print('Еще раз попробуй')

# def victory_check(board):
#     victory = ((0,1,2),(3,4,5),(6,7,8),
#                (0,3,6),(1,4,7),(2,5,8),
#                (0,4,8),(2,4,6))
#     for i in victory:
#         if board[i[0]] == board[i[1]] == board[i[2]]:
#             return board[i[0]]
#     return False

# def game(board):
#     counter =0
#     vic = False
#     while not vic:
#         design_board(board)
#         if counter % 2 == 0:
#             choice('X')
#         else:
#             choice('0')
#         counter +=1
#         if counter > 4:
#             tt_win = victory_check(board)
#             if tt_win:
#                 print(tt_win,'Победа')
#                 vic = True
#                 break
#             if counter == 9:
#                 print('Победила, ДРУЖБА)')
#         design_board(board)
# game(board)

#с PIP

from tkinter import *
import random


class Square:
    """ задает квадраты(клетки) """
    def __init__(self, master, root, num, row, column):
        self.master = master
        self.square_num = num
        self.msg = StringVar()
        self.lbl = Label(root, textvariable=self.msg, font="FreeSerifBold 75", bg="white")
        self.lbl.grid(row=row, column=column, sticky=NSEW, padx=5, pady=5)

    def unbind(self):
        self.lbl.unbind("<Button-1>")

    def bind(self):
        self.lbl.bind("<Button-1>", self.choice)

    def bind_comp(self):
        self.lbl.bind("<Button-1>", self.choice_comp)

    def set_msg(self, txt):
        self.msg.set(txt)

    def choice(self, event):
        self.master.turn_user(self.square_num)

    def choice_comp(self, event):
        self.master.turn_pc()

    def cfg(self, color):
        self.lbl.configure(bg=color)


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.master = master
        self.master.config(bg="#D9D9D9")
        # константы
        self.wins = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                     (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        self.board_start = ['_'] * 9
        self.free_squares_start = [x for x in range(9)]
        self.choice_pc1 = [0, 2, 6, 8]
        self.choice_pc2 = [1, 3, 5, 7]
        # статистика игры
        self.drawn_game = 0
        self.user1_win = 0
        self.user2_win = 0
        self.pc1_win = 0
        self.pc2_win = 0
        self.create_widgets()

    def create_widgets(self):
        # блок статистики
        stat_frame = Frame(self.master)
        stat_frame.grid(row=0, column=0, padx=5, pady=5, sticky=N)
        # статистика
        statistics = LabelFrame(stat_frame, text=" Статистика ")
        statistics.grid()
        self.stat_msg = StringVar()
        stat_lbl = Label(statistics, textvariable=self.stat_msg, justify=LEFT, width=20)
        stat_lbl.grid(padx=0)
        self.stat_msg.set(
            'Сыграно игр: %s\nИз них:\n  побед игрока 1: %s\n  побед игрока 2: %s\n  побед компьютера 1: %s\n  побед компьютера 2: %s\n  ничьих: %s' %
            (self.user1_win + self.user2_win + self.pc1_win + self.pc2_win + self.drawn_game,
             self.user1_win, self.user2_win, self.pc1_win, self.pc2_win, self.drawn_game)
        )
        # блок игрока 1
        gamer1_frame = Frame(self.master)
        gamer1_frame.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        step_choice = LabelFrame(gamer1_frame, text=" Игрок 1 ")
        step_choice.grid(ipadx=26)
        self.gamer1_step = IntVar()
        self.gamer1_step.set(0)
        gamer1_step0 = Radiobutton(step_choice, text='Игрок', variable=self.gamer1_step, value=0)
        gamer1_step1 = Radiobutton(step_choice, text='Компьютер', variable=self.gamer1_step, value=1)
        gamer1_step0.grid(ipady=2, sticky=W)
        gamer1_step1.grid(ipady=3, sticky=W)
        # блок игрока 2
        gamer2_frame = Frame(self.master)
        gamer2_frame.grid(row=1, column=1, padx=5, pady=5, sticky=W)
        step_choice = LabelFrame(gamer2_frame, text=" Игрок 2 ")
        step_choice.grid(ipadx=26)
        self.gamer2_step = IntVar()
        self.gamer2_step.set(1)
        gamer2_step0 = Radiobutton(step_choice, text='Игрок', variable=self.gamer2_step, value=0)
        gamer2_step1 = Radiobutton(step_choice, text='Компьютер', variable=self.gamer2_step, value=1)
        gamer2_step0.grid(ipady=2, sticky=W)
        gamer2_step1.grid(ipady=3, sticky=W)
        # блок выбора хода
        step_frame = Frame(self.master)
        step_frame.grid(row=0, column=1, padx=10, pady=5, sticky=N)
        step_choice = LabelFrame(step_frame, text=" Ходит первым ")
        step_choice.grid(ipadx=20, ipady=25)
        self.first_step = IntVar()
        self.first_step.set(0)
        first_step0 = Radiobutton(step_choice, text='Игрок 1', variable=self.first_step, value=0)
        first_step1 = Radiobutton(step_choice, text='Игрок 2', variable=self.first_step, value=1)
        first_step0.grid(ipady=3, sticky=W)
        first_step1.grid(ipady=2, sticky=W)
        # блок выбора знака
        sign_frame = Frame(self.master)
        sign_frame.grid(row=0, column=2, padx=5, pady=5)
        # выбор знака
        sign_choice = LabelFrame(sign_frame, text=" Выбор знака ")
        sign_choice.grid(ipadx=20)
        self.gamer1_choice = StringVar()
        self.gamer1_choice.set('0')
        gamer1_sign0 = Radiobutton(sign_choice, text='Игрок 1 "0"', variable=self.gamer1_choice, value='0')
        gamer1_sign1 = Radiobutton(sign_choice, text='Игрок 1 "X"', variable=self.gamer1_choice, value='X')
        gamer1_sign0.grid()
        gamer1_sign1.grid()
        # кнопка старт
        self.btn = Button(sign_frame, text="Старт")
        self.btn.bind("<Button-1>", self.start)
        self.btn.grid(pady=6, ipady=10, sticky=NSEW)
        # игровое поле
        self.squares = {}
        num = 0
        for row in range(2, 5):
            for column in range(0, 3):
                self.squares[num] = Square(self, self.master, num, row, column)
                num += 1
        self.widgets = [gamer1_sign0, gamer1_sign1, gamer1_step0, gamer1_step1, gamer2_step0, gamer2_step1, first_step0,
                        first_step1, self.btn]

    def start(self, *args):
        self.choice_pc = None
        self.flag_end = False
        self.flag_choice_user = False
        self.flag_choice_pc = False
        self.free_squares = self.free_squares_start[:]
        self.board = self.board_start[:]
        for square_num in range(9):
            square = self.squares[square_num]
            if self.gamer1_step.get() == 1 and self.gamer2_step.get() == 1:
                square.bind_comp()
            else:
                square.bind()
            square.set_msg('')
            square.cfg('white')
        gs1 = self.gamer1_step.get()
        gs2 = self.gamer2_step.get()
        if self.gamer1_choice.get() == '0':
            if gs1 == 0 and gs2 == 1:
                self.user_sign, self.pc_sign = '0', 'X'
            elif gs1 == 1 and gs2 == 0:
                self.pc_sign, self.user_sign = '0', 'X'
            elif gs1 == 0 and gs2 == 0:
                self.user1_sign, self.user2_sign = '0', 'X'
            elif gs1 == 1 and gs2 == 1:
                self.pc1_sign, self.pc2_sign = '0', 'X'
        else:
            if gs1 == 0 and gs2 == 1:
                self.user_sign, self.pc_sign = 'X', '0'
            elif gs1 == 1 and gs2 == 0:
                self.pc_sign, self.user_sign = 'X', '0'
            elif gs1 == 0 and gs2 == 0:
                self.user1_sign, self.user2_sign = 'X', '0'
            elif gs1 == 1 and gs2 == 1:
                self.pc1_sign, self.pc2_sign = 'X', '0'
        fs = self.first_step.get()
        if fs == 0:
            if gs1 == 1:
                self.turn_pc()
        elif fs == 1:
            if gs2 == 1:
                self.flag_choice_pc = True
                self.turn_pc()
        self.widget_state()
        self.btn.unbind("<Button-1>")

    def widget_state(self, wst=DISABLED):
        for widget in self.widgets:
            widget.config(state=wst)

    def unbind_squares(self):
        for square_num in self.free_squares:
            self.squares[square_num].unbind()

    def greet_winner(self, sign):
        """ поздравления """
        if self.gamer1_step.get() == 0 and self.gamer2_step.get() == 0:
            if sign == self.user1_sign and self.gamer1_step.get() == 0:
                self.user1_win += 1
            if sign == self.user2_sign and self.gamer2_step.get() == 0:
                self.user2_win += 1
        elif self.gamer1_step.get() == 1 and self.gamer2_step.get() == 1:
            if sign == self.pc1_sign and self.gamer1_step.get() == 1:
                self.pc1_win += 1
            elif sign == self.pc2_sign and self.gamer2_step.get() == 1:
                self.pc2_win += 1
        else:
            if sign == self.user_sign and self.gamer1_step.get() == 0:
                self.user1_win += 1
            if sign == self.pc_sign and self.gamer1_step.get() == 1:
                self.pc1_win += 1
            if sign == self.user_sign and self.gamer2_step.get() == 0:
                self.user2_win += 1
            if sign == self.pc_sign and self.gamer2_step.get() == 1:
                self.pc2_win += 1
        self.flag_end = True

    def show_win(self, win, sign):
        if self.gamer1_step.get() == 0 and self.gamer2_step.get() == 0:
            if sign == self.user1_sign:
                color = 'green'
            else:
                color = 'red'
        elif self.gamer1_step.get() == 1 and self.gamer2_step.get() == 1:
            if sign == self.pc1_sign:
                color = 'green'
            else:
                color = 'red'
        else:
            if sign == self.user_sign:
                color = 'green'
            else:
                color = 'red'
        for square_num in win:
            square = self.squares[square_num]
            square.cfg(color)

    def game_over(self):
        """ окончание игры """
        self.stat_msg.set(
            'Сыграно игр: %s\nИз них:\n  побед игрока 1: %s\n  побед игрока 2: %s\n  побед компьютера 1: %s\n  побед компьютера 2: %s\n  ничьих: %s' %
            (self.user1_win + self.user2_win + self.pc1_win + self.pc2_win + self.drawn_game,
             self.user1_win, self.user2_win, self.pc1_win, self.pc2_win, self.drawn_game)
        )
        self.widget_state(NORMAL)
        self.btn.bind("<Button-1>", self.start)

    def test_win(self, sign):
        for a, b, c in self.wins:
            if self.board[a] == sign and self.board[b] == sign and self.board[c] == sign:
                self.show_win((a, b, c), sign)
                self.unbind_squares()
                self.greet_winner(sign)
                self.game_over()
                return
        if not self.free_squares:
            self.flag_end = True
            self.drawn_game += 1
            for square_num in range(9):
                square = self.squares[square_num]
                square.cfg('yellow')
            self.game_over()

    def is_win(self, sign, iboard):
        for a, b, c in self.wins:
            if iboard[a] == sign and iboard[b] == sign and iboard[c] == sign:
                return True
        return False

    def find_best_turn(self, sign):
        for iturn in self.free_squares:
            iboard = self.board[:]
            iboard[iturn] = sign
            res = self.is_win(sign, iboard)
            if res:
                return iturn
        return None

    def default_choice(self):
        if not self.choice_pc:
            self.choice_pc = [4]
            random.shuffle(self.choice_pc1)
            random.shuffle(self.choice_pc2)
            self.choice_pc.extend(self.choice_pc1)
            self.choice_pc.extend(self.choice_pc2)
        for iturn in self.choice_pc:
            if iturn in self.free_squares:
                return iturn

    def turn_pc(self):
        """ ход пк """
        if self.gamer1_step.get() == 1 and self.gamer2_step.get() == 1:
            if not self.flag_choice_pc:
                square_num = self.find_best_turn(self.pc1_sign)
                if square_num is None:
                    square_num = self.find_best_turn(self.pc2_sign)
                    if square_num is None:
                        square_num = self.default_choice()
                self.turn(square_num, self.pc1_sign)
                self.flag_choice_pc = True
            else:
                square_num = self.find_best_turn(self.pc2_sign)
                if square_num is None:
                    square_num = self.find_best_turn(self.pc1_sign)
                    if square_num is None:
                        square_num = self.default_choice()
                self.turn(square_num, self.pc2_sign)
                self.flag_choice_pc = False
        else:
            square_num = self.find_best_turn(self.pc_sign)
            if square_num is None:
                square_num = self.find_best_turn(self.user_sign)
                if square_num is None:
                    square_num = self.default_choice()
            self.turn(square_num, self.pc_sign)

    def change_board(self, square_num, sign):
        """ заполнение клетки знаком """
        self.board[square_num] = sign
        self.free_squares.remove(square_num)
        if self.gamer1_step.get() == 0 and self.gamer2_step.get() == 0:
            self.flag_choice_user = True

    def turn(self, square_num, sign):
        square = self.squares[square_num]
        square.unbind()
        square.set_msg(sign)
        self.change_board(square_num, sign)
        self.test_win(sign)

    def turn_user(self, square_num):
        """ ход игрока """
        if self.gamer1_step.get() == 0 and self.gamer2_step.get() == 0:
            if self.first_step.get() == 0:
                if not self.flag_choice_user:
                    self.turn(square_num, self.user1_sign)
                else:
                    self.turn(square_num, self.user2_sign)
                    self.flag_choice_user = False
            elif self.first_step.get() == 1:
                if not self.flag_choice_user:
                    self.turn(square_num, self.user2_sign)
                else:
                    self.turn(square_num, self.user1_sign)
                    self.flag_choice_user = False
        elif (self.gamer1_step.get() == 0 and self.gamer2_step.get() == 1) or (
                self.gamer1_step.get() == 1 and self.gamer2_step.get() == 0):
            self.turn(square_num, self.user_sign)
            if not self.flag_end:
                self.turn_pc()


def main():
    root = Tk()
    root.title('Крестики - Нолики')
    root.resizable(FALSE, FALSE)
    app = Application(root)
    root.mainloop()


if __name__ == '__main__':
    main()