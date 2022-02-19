from src.scripts import interface
from src.screens.Loader.main import LoaderScreen
from src.screens.Authentication.Sign_In.main import SignInScreen
# from src.screens.Eyetesting.EyeTester.main import eyeTesting
# from src.screens.Instructions.frontend.frontend import Frontend


def startApp():
    window = interface.UserInterface()

    LoaderScreen(window)

    SignInScreen(window)

    window.run()