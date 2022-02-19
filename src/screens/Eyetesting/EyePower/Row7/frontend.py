from tkinter import *
from src.screens.Eyetesting.EyePower.Row8.frontend import Row8
from src.screens.Eyetesting.EyePower.Row7.backend import results

class Row7:
    def __init__(self,root, Interface_Frame, Interface_Label, Interface_Button):
        """ Eye Power calculation Screen """
        
        self.eyePowerScreen = Interface_Frame(
            root, 0, 0, 1000, 600, "white")

        Interface_Label(self.eyePowerScreen, "src/images/frontend/Visual Acuity/Para.png", 450, 50, CENTER, "white", 500, 21)

        Interface_Label(self.eyePowerScreen, "src/images/frontend/Visual Acuity/Para2.png", 450, 90, CENTER, "white", 500, 24)

        Interface_Label(self.eyePowerScreen, "src/images/frontend/Visual Acuity/Row7.png",450, 300, CENTER, "white", 406, 63)

        # Next Button
        Interface_Button(
            self.eyePowerScreen, "src/images/frontend/Onboarding/Button.png", 150, 39, "white", FLAT, 350, 530, CENTER, lambda: Row8(root, Interface_Frame, Interface_Label, Interface_Button))

        Interface_Button(
            self.eyePowerScreen, "src/images/frontend/Visual Acuity/Button.png", 150, 39, "white", FLAT, 550, 530, CENTER, lambda: results(root,Interface_Frame,Interface_Label))
        