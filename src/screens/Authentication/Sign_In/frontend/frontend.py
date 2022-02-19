from tkinter import *
from src.screens.Authentication.Sign_In.backend import backend
from src.screens.Authentication.Sign_Up.frontend import frontend


class Frontend:
    def __init__(self, window):
        self.window = window
        self.loginScreen = self.window.Interface_Frame(
            self.window.root, 0, 0, 1000, 600, "white")

        # Header Vector
        self.window.Interface_Label(
            self.loginScreen, "src/images/frontend/User Authentication/Vector1.png", 840, 40, CENTER, "white", 214, 231)

        # Paragraph
        self.window.Interface_Label(
            self.loginScreen, "src/images/frontend/User Authentication/Paragraph.png", 170, 60, CENTER, "white", 300, 87)

        # Email Text
        self.window.Interface_Label(
            self.loginScreen, "src/images/frontend/User Authentication/EmailText.png", 170, 160, CENTER, "white", 100, 9)

        # Email Entry Input
        self.emailInput = self.window.Interface_Input(
            self.loginScreen, "white", 2, 60, FLAT, "Segoe UI", 16, "", "#FF5151", "#FF5151", 110, 180, 50, "")

        # Password Text
        self.window.Interface_Label(
            self.loginScreen, "src/images/frontend/User Authentication/PasswordText.png", 150, 260, CENTER, "white", 60, 9)

        # Email Entry Input
        self.passwordInput = self.window.Interface_Input(
            self.loginScreen, "white", 2, 60, FLAT, "Segoe UI", 16, "", "#FF5151", "#FF5151", 110, 280, 50, "*")

        # Sign In Button
        self.window.Interface_Button(self.loginScreen, "src/images/frontend/User Authentication/SIGN-IN_Button.png",
                                     300, 48, "white", FLAT, 450, 410, CENTER, lambda:backend.Backend(self.emailInput, self.passwordInput, self.window).signIn())

        # Register Text
        self.window.Interface_Label(
            self.loginScreen, "src/images/frontend/User Authentication/RegisterText.png", 450, 480, CENTER, "white", 200, 13)

        # Register Button
        self.window.Interface_Button(
            self.loginScreen, "src/images/frontend/User Authentication/Register.png", 59, 16, "white", FLAT, 450, 520, CENTER, lambda: frontend.Frontend(self.window, self.loginScreen))

        # Footer Vector
        self.window.Interface_Label(
            self.loginScreen, "src/images/frontend/User Authentication/Vector2.png", 60, 540, CENTER, "white", 232, 239)

