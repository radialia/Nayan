from tkinter import *
from src.screens.Onboarding.Second.frontend import frontend

class Frontend:
    def __init__(self, root, window):
        """ First slide of the onboarding """
        self.root = root
        self.window = window

        firstScreen = self.window.Interface_Frame(
            self.root, 0, 0, 1000, 600, "white")

        # Header Vector
        self.window.Interface_Label(
            firstScreen, "src/images/frontend/Onboarding/ImageContainer.png", 450, 150, CENTER, "white", 404, 365)

        # Indicator
        self.window.Interface_Label(
            firstScreen, "src/images/frontend/Onboarding/Indicator1.png", 450, 310, CENTER, "white", 107, 10)

        # Paragraph
        self.window.Interface_Label(
            firstScreen, "src/images/frontend/Onboarding/Paragraph1.png", 450, 410, CENTER, "white", 539, 170)

        # Next Button
        self.window.Interface_Button(
            firstScreen, "src/images/frontend/Onboarding/Button.png", 150, 39, "white", FLAT, 450, 530, CENTER, lambda: frontend.Frontend(self.root, self.window))
