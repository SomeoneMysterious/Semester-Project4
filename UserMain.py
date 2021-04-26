from network import Network
from tkinter import *
import time


class Player(object):

    def __init__(self):
        self.tk = Tk()
        self.frame = Frame(self.tk)
        self.frame.grid()
        self.message = Entry(self.frame)
        self.message.grid(row=0, column=0, columnspan=3, sticky=W)
        self.tk.mainloop()


if __name__ == "__main__":
    player = Player()
    time.sleep(5)
