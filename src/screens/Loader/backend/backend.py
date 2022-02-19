from tkinter import *
from tkinter.ttk import Progressbar
from time import sleep

class Backend:
    def __init__(self, root):
        """ Creates a progress bar """
        self.progressbar = Progressbar(
            root, orient=HORIZONTAL, length=600, mode="determinate")

        self.progressbar.place(x=450, y=300, anchor=CENTER)

        self.loader(root)

    def loader(self, root):
        """ Updates and progress the progress bar every 0.3s """
        try:
            for i in range(100):
                root.update()

                self.progressbar['value'] += 1
                sleep(0.02)
        except:
            print("Ran into an Error! Try again later!")