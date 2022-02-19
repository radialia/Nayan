from tkinter import *
from tkinter import messagebox
import pyrebase
from src.screens.Onboarding.First.main import FisrtScreen

class Backend:
    def __init__(self, emailInput, passwordInput0, passwordInput, root, window):
        self.emailInput = emailInput
        self.passwordInput = passwordInput
        self.passwordInput0 = passwordInput0
        self.root = root
        self.window = window

        firebaseConfig = {
            "apiKey": "AIzaSyAeuKaIJCAVDz1qHIr4wUqb4D8FW_0nUlw",
            "authDomain": "nayan-46299.firebaseapp.com",
            "databaseURL": "https://nayan-46299-default-rtdb.firebaseio.com",
            "projectId": "nayan-46299",
            "storageBucket": "nayan-46299.appspot.com",
            "messagingSenderId": "122580618009",
            "appId": "1:122580618009:web:1c3bb274b8ed5a92371388",
            "measurementId": "G-LLT1MFQWTZ"
        }

        # Initialisation of the firebase configuration and unpack the values
        self.firebase = pyrebase.initialize_app(firebaseConfig)
        self.email, self.password = self.emailInput.get(), self.passwordInput.get()

    def signUp(self):
        auth = self.firebase.auth()

        if(self.passwordInput0.get() == self.passwordInput.get()):
            if(self.email and self.password and self.passwordInput0.get()):
                try:
                    auth.create_user_with_email_and_password(self.email, self.password)
                    messagebox.showinfo(
                        "Success", "User signed up successfully")
                    FisrtScreen(self.root, self.window)
                except:
                    messagebox.showerror("Error", "User already exits")
            elif(self.email or self.password):
                messagebox.showerror("Error", "All fields are required!")
        elif(self.passwordInput0.get() != self.passwordInput.get()):
            messagebox.showerror(
                "Error", "Set Password and Confirm Password needs to be same")
        else:
            messagebox.showerror(
                "Error", "Something went wrong! Try again and make sure to input a vaild email address")

        # Empty the fields
        self.emailInput.delete(0, END)
        self.passwordInput0.delete(0, END)
        self.passwordInput.delete(0, END)