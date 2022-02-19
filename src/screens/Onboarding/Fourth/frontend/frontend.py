from tkinter import *
from src.screens.Instructions.frontend import frontend


class Frontend():
    def __init__(self, root, window):
        """ Fourth slide of the onboarding screen """
        self.root = root
        self.window = window

        self.fourthScreen = self.window.Interface_Frame(
            root, 0, 0, 1000, 600, "white")

        # Header Vector
        self.window.Interface_Label(
            self.fourthScreen, "src/images/frontend/Onboarding/ImageContainer4.png", 450, 150, CENTER, "white", 427, 262)

        # Indicator
        self.window.Interface_Label(
            self.fourthScreen, "src/images/frontend/Onboarding/Indicator4.png", 450, 310, CENTER, "white", 106, 10)

        # Paragraph
        self.window.Interface_Label(
            self.fourthScreen, "src/images/frontend/Onboarding/Paragraph4.png", 450, 410, CENTER, "white", 557, 170)

        # Done button
        self.window.Interface_Button(
            self.fourthScreen, "src/images/frontend/Onboarding/Button2.png", 150, 39, "white", FLAT, 450, 530, CENTER, lambda: frontend.Frontend(self.window.Interface_Frame, self.window.Interface_Label, self.window.Interface_Button, self.window.root))
