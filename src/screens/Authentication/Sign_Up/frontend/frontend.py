from tkinter import *
from src.screens.Authentication.Sign_Up.backend import backend

class Frontend():
    def __init__(self, root, screen):
        """ Creates the sign up screen """
        self.root = root
        self.screen = screen

        # Basic sign up screen frame
        self.signupScreen = self.root.Interface_Frame(
            self.screen, 0, 0, 1000, 600, "white")

        # Header Vector
        self.root.Interface_Label(
            self.signupScreen, "src/images/frontend/User Authentication/Vector1.png", 840, 40, CENTER, "white", 214, 231)

        # Paragraph
        self.root.Interface_Label(
            self.signupScreen, "src/images/frontend/User Authentication/Paragraph2.png", 190, 50, CENTER, "white", 323, 117)

        # Email Text
        self.root.Interface_Label(
            self.signupScreen, "src/images/frontend/User Authentication/EmailText.png", 170, 140, CENTER, "white", 100, 9)

        # Email Entry Input
        self.emailInput = self.root.Interface_Input(
            self.signupScreen, "white", 2, 60, FLAT, "Segoe UI", 16, "", "#FF5151", "#FF5151", 110, 160, 50, "")

        # Set Password Text
        self.root.Interface_Label(
            self.signupScreen, "src/images/frontend/User Authentication/SetPasswordText.png", 150, 240, CENTER, "white", 60, 9)

        # Set Password Entry Input
        self.passwordInput0 = self.root.Interface_Input(
            self.signupScreen, "white", 2, 60, FLAT, "Segoe UI", 16, "", "#FF5151", "#FF5151", 110, 260, 50, "*")

        # Current Password Text
        self.root.Interface_Label(
            self.signupScreen, "src/images/frontend/User Authentication/ConfirmPasswordText.png", 160, 340, CENTER, "white", 80, 9)

        # Current Password Entry Input
        self.passwordInput = self.root.Interface_Input(
            self.signupScreen, "white", 2, 60, FLAT, "Segoe UI", 16, "", "#FF5151", "#FF5151", 110, 360, 50, "*")

        # Sign Up Button
        self.root.Interface_Button(self.signupScreen, "src/images/frontend/User Authentication/_Button.png",
                                   300, 48, "white", FLAT, 450, 460, CENTER, lambda:backend.Backend(self.emailInput,self.passwordInput0, self.passwordInput, self.screen, self.root).signUp(), )

        # Sign In Text
        self.root.Interface_Label(
            self.signupScreen, "src/images/frontend/User Authentication/RegisterText2.png", 450, 520, CENTER, "white", 200, 18)

        # Sign In Button
        self.root.Interface_Button(
            self.signupScreen, "src/images/frontend/User Authentication/Register2.png", 59, 18, "white", FLAT, 450, 550, CENTER, lambda:self.signupScreen.destroy())

        # Footer Vector
        self.root.Interface_Label(
            self.signupScreen, "src/images/frontend/User Authentication/Vector2.png", 60, 540, CENTER, "white", 232, 239)
