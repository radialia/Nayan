from tkinter import *
from tkinter import messagebox
import pyrebase
from src.screens.Instructions.frontend.frontend import Frontend


class Backend:
    def __init__(self, emailInput, passwordInput, window):
        self.emailInput = emailInput
        self.passwordInput = passwordInput
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

    def signIn(self):
        auth = self.firebase.auth()

        if(self.email and self.password):
            try:
                auth.sign_in_with_email_and_password(self.email, self.password)
                messagebox.showinfo("Success", "User logged in successfully")
                Frontend(self.window.Interface_Frame, self.window.Interface_Label, self.window.Interface_Button, self.window.root, self.window)
            except:
                messagebox.showerror("Error", "Invalid Email or Password")
        elif(self.email or self.password):
            messagebox.showerror("Error", "All fields are required!")

        self.emailInput.delete(0, END)
        self.passwordInput.delete(0, END)
