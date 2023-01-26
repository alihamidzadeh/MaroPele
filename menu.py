import sys
import os
from tkinter import *


class GUI:

    def __init__(self):
        self.root = None
        self.bg = None
        self.label1 = None
        self.startButton = None
        self.exitButton = None

    def root_window(self):
        self.root = Tk()

        self.root.title("Snake And Ladder")
        self.root.resizable(width=True,
                            height=True)
        self.root.configure(width=512,
                            height=512)

        self.bg = PhotoImage(file="images/9.png")

        self.label1 = Label(self.root, image=self.bg)
        self.label1.place(x=0, y=0)

        self.startButton = Button(self.root, text="New Game", background='#DB1F48',foreground='white', font=("showcard gothic", 16, "bold"),
                                  command=self.start_game)
        self.startButton.place(x=90,
                               y=400,
                               width=140,
                               height=100)

        self.exitButton = Button(self.root, text="Exit", background='#DB1F48',foreground='white', font=("showcard gothic", 16, "bold"),
                                 command=self.exit)
        self.exitButton.place(x=280,
                              y=400,
                              width=140,
                              height=100)

        self.root.mainloop()

    def start_game(self):
        self.root.destroy()
        os.system(f'python main.py')

    def exit(self):
        sys.exit()
main = GUI()
main.root_window()
