from tkinter import *


class Frontend:
    def __init__(self, window):
        """ User Interface for the loader screen """
        window.Interface_Label(root=window.root, path="src/images/frontend/Logo.png",
                            x_pos=450, y_pos=200, anchor=CENTER, bgColor="white", width=350, height=118)
