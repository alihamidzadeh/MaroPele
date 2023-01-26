import random
import time
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter.filedialog import asksaveasfile








def save_game():
    global turn, pos1, pos2, flag_start1, flag_start2

    try:

        f = asksaveasfile(initialfile='game.txt',
                          defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        f.write(f'{turn}\n{pos1}\n{pos2}\n{flag_start1}\n{flag_start2}\n')
        f.close()
        messagebox.showinfo("Save", "The game was Saved")

    except (AttributeError, FileNotFoundError) as err:
        print(err)




def load_game():
    global turn, pos1, pos2, flag_start1, flag_start2

    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    try:

        filename = fd.askopenfilename(title='Open a file', initialdir='/', filetypes=filetypes)

        f = open(filename, "r")
        turn = int(f.readline().replace('\n', ''))
        pos1 = int(f.readline().replace('\n', ''))
        pos2 = int(f.readline().replace('\n', ''))
        flag_start1 = f.readline().replace('\n', '')
        flag_start2 = f.readline().replace('\n', '')

        if flag_start1 == "True":
            flag_start1 = True
        else:
            flag_start1 = False

        if flag_start2 == "True":
            flag_start2 = True
        else:
            flag_start2 = False


        if flag_start1:
            move_player(1, pos1)

        if flag_start2:
            move_player(2, pos2)

        if turn == 2:
            b1.configure(state='disabled')
            b2.configure(state='normal')
        else:
            b1.configure(state='normal')
            b2.configure(state='disabled')
        f.close()
        messagebox.showinfo("Load", "The game was Loaded")

    except FileNotFoundError as err:
        print(err)

def start_game():
    global dice, b1, b2, b5, b6

    dice = PhotoImage(file="images/2.png")
    b3 = Button(root, image=dice, height=80, width=125)

    b4 = Button(root, text="Exit", height=2, width=8, fg="black", bg='green', font=("showcard gothic", 16, "bold"),
                activebackground='red', command=root.destroy)

    yy = 20
    b1.place(x=800, y=yy + 250)
    b2.place(x=800, y=yy + 350)
    b3.place(x=800, y=yy + 150)
    b4.place(x=800, y=yy + 60)
    b5.place(x=790, y=yy)
    b6.place(x=870, y=yy)


def reset_players():
    global player1, player2, pos1, pos2
    player1.place(x=0, y=600)
    player2.place(x=50, y=600)
    pos1 = 0
    pos2 = 0


def load_dice_images():
    global Dice
    names = ['images/3.png', 'images/4.png', 'images/5.png', 'images/6.png', 'images/7.png', 'images/8.png']
    for name in names:
        dice = PhotoImage(file=name)
        Dice.append(dice)


def roll_dice():
    global Dice, turn, pos1, pos2, b1, b2, flag_start1, flag_start2
    r = random.randint(1, 6)
    b3 = Button(root, image=Dice[r - 1], height=80, width=125)
    b3.place(x=800, y=170)
    # print(f'player {turn} get {r}')
    roll_log.set(f'player {turn} get {r}')  # display roll dice log
    if turn == 1:
        if r == 6 and flag_start1:
            if pos1 + 6 <= 100:
                pos1 += 6

        if r == 6 and flag_start1 == False:
            flag_start1 = True
            pos1 = 1
            move_player(turn, pos1)
            # turn = 2 TODO for again roll dice after Enter the game
            # b1.configure(state='disabled')
            # b2.configure(state='normal')

        if r != 6 and flag_start1:
            if pos1 + r <= 100:
                pos1 += r
            check_ladder(turn)
            check_snake(turn)
            move_player(turn, pos1)

            turn = 2
            b1.configure(state='disabled')
            b2.configure(state='normal')

        if r != 6 and not flag_start1:
            turn = 2
            b1.configure(state='disabled')
            b2.configure(state='normal')


    elif turn == 2:

        if r == 6 and flag_start2:
            if pos2 + 6 <= 100:
                pos2 += 6

        if r == 6 and flag_start2 == False:
            flag_start2 = True
            pos2 = 1
            move_player(turn, pos2)
            # turn = 1  TODO for again roll dice after Enter the game
            # b1.configure(state='normal')
            # b2.configure(state='disabled')

        if r != 6 and flag_start2:
            if pos2 + r <= 100:
                pos2 += r
            check_ladder(turn)
            check_snake(turn)
            move_player(turn, pos2)
            turn = 1
            b1.configure(state='normal')
            b2.configure(state='disabled')

        if r != 6 and not flag_start2:
            turn = 1
            b1.configure(state='normal')
            b2.configure(state='disabled')

    is_winner()


def is_winner():
    global pos1, pos2

    if pos1 == 100:
        messagebox.showinfo("finish", "Player1 is the Winner")
        reset_players()

    elif pos2 == 100:
        messagebox.showinfo("finish", "Player2 is the Winner")
        reset_players()


def move_player(turn, r):
    global player1, player2, index
    if turn == 1:
        player1.place(x=index[r][0], y=index[r][1])
    elif turn == 2:
        player2.place(x=index[r][0], y=index[r][1])


def check_ladder(turn):
    global pos1, pos2, ladder
    f = 0
    if turn == 1:
        if pos1 in ladder:
            pos1 = ladder[pos1]
            f = 1

    else:
        if pos2 in ladder:
            pos2 = ladder[pos2]
            f = 1

    return f


def check_snake(turn):
    global pos1, pos2

    if turn == 1:
        if pos1 in snake:
            pos1 = snake[pos1]
            f = 1

    else:
        if pos2 in snake:
            pos2 = snake[pos2]


index = {100: (25, 20), 99: (100, 20), 98: (175, 20), 97: (250, 20), 96: (325, 20), 95: (400, 20), 94: (480, 20),
         93: (565, 20), 92: (635, 20), 91: (720, 20), 81: (25, 80), 82: (100, 80), 83: (175, 80), 84: (250, 80),
         85: (335, 80), 86: (410, 80), 87: (485, 80), 88: (570, 80), 89: (645, 80), 90: (720, 80), 80: (25, 140),
         79: (100, 140), 78: (175, 140), 77: (250, 140), 76: (325, 140), 75: (420, 140), 74: (495, 140), 73: (570, 140),
         72: (645, 140), 71: (720, 140), 61: (25, 200), 62: (100, 200), 63: (175, 200), 64: (250, 200), 65: (335, 200),
         66: (410, 200), 67: (485, 200), 68: (560, 200), 69: (645, 200), 70: (720, 200), 60: (25, 260), 59: (100, 260),
         58: (175, 260), 57: (260, 260), 56: (335, 260), 55: (410, 260), 54: (485, 260), 53: (560, 260), 52: (635, 260),
         51: (720, 260), 41: (25, 320), 42: (100, 320), 43: (175, 320), 44: (250, 320), 45: (335, 320), 46: (410, 320),
         47: (485, 320), 48: (570, 320), 49: (645, 320), 50: (720, 320), 40: (25, 380), 39: (100, 380), 38: (175, 380),
         37: (250, 380), 36: (335, 380), 35: (410, 380), 34: (485, 380), 33: (570, 380), 32: (645, 380), 31: (720, 380),
         21: (25, 440), 22: (100, 440), 23: (175, 440), 24: (260, 440), 25: (335, 440), 26: (410, 440), 27: (485, 440),
         28: (570, 440), 29: (645, 440), 30: (720, 440), 20: (25, 500), 19: (100, 500), 18: (175, 500), 17: (250, 500),
         16: (335, 500), 15: (410, 500), 14: (485, 500), 13: (570, 500), 12: (645, 500), 11: (720, 500), 1: (25, 560),
         2: (100, 560), 3: (175, 560), 4: (260, 560), 5: (335, 560), 6: (410, 560), 7: (485, 560), 8: (570, 560),
         9: (645, 560), 10: (720, 560)}

Dice = []
ladder = {8: 29, 19: 57, 26: 45, 46: 97, 50: 69, 60: 79, 73: 92}
snake = {99: 43, 94: 66, 85: 55, 70: 13, 63: 25, 48: 6, 39: 3}
pos1 = None
pos2 = None
flag_start1 = False
flag_start2 = False
root = Tk()
root.title("Snake and Ladder")
root.geometry("950x640")
root.wm_attributes("-topmost", 1)  # set always on top
bg = PhotoImage(file="images/1.png")
label1 = Label(root, image=bg)
label1.place(x=0, y=0)

b1 = Button(root, text="Player1", height=2, width=8, fg="black", bg='blue', font=("showcard gothic", 16, "bold"),
            activebackground='blue', command=roll_dice)
b2 = Button(root, text="Player2", height=2, width=8, fg="black", bg='red', font=("showcard gothic", 16, "bold"),
            activebackground='red', command=roll_dice)

b2.configure(state='disabled')

b5 = Button(root, text="Save", height=1, width=4, fg="red", bg='yellow', font=("showcard gothic", 16, "bold"),
            activebackground='red', command=save_game)

b6 = Button(root, text="Load", height=1, width=4, fg="red", bg='yellow', font=("showcard gothic", 16, "bold"),
            activebackground='red', command=load_game)

roll_log = StringVar()
label2 = Label(root, textvariable=roll_log, bg='green', font=('Cursive', 16, 'bold'))
label2.place(x=400, y=605)

player1 = Canvas(root, width=30, height=30)
player1.create_oval(10, 10, 30, 30, fill='blue')
player1.place(x=0, y=600)

player2 = Canvas(root, width=30, height=30)
player2.create_oval(10, 10, 30, 30, fill='red')
player2.place(x=50, y=600)
turn = 1

reset_players()
load_dice_images()
start_game()

root.mainloop()
