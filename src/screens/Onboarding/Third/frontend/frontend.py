from tkinter import *
from src.screens.Onboarding.Fourth.frontend import frontend

class Frontend():
    def __init__(self, root, window):
        """ Third slide of the onboarding screen """
        self.root = root
        self.window = window

        self.thirdScreen = self.window.Interface_Frame(
            root, 0, 0, 1000, 600, "white")

        # Header Vector
        self.window.Interface_Label(
            self.thirdScreen, "src/images/frontend/Onboarding/ImageContainer3.png", 450, 150, CENTER, "white", 427, 299)

        # Indicator
        self.window.Interface_Label(
            self.thirdScreen, "src/images/frontend/Onboarding/Indicator3.png", 450, 310, CENTER, "white", 107, 10)

        # Paragraph
        self.window.Interface_Label(
            self.thirdScreen, "src/images/frontend/Onboarding/Paragraph3.png", 450, 410, CENTER, "white", 544, 170)

        # Next Button
        self.window.Interface_Button(
            self.thirdScreen, "src/images/frontend/Onboarding/Button.png", 150, 39, "white", FLAT, 450, 530, CENTER, lambda: frontend.Frontend(self.root, self.window))
