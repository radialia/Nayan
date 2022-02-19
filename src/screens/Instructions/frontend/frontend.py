from tkinter import *
from src.screens.Eyetesting.DistanceScreen.frontend.frontend import DistanceScreen


class Frontend:
    def __init__(self, Interface_Frame, Interface_Label, Interface_Button, root, camera):
        """ Instructions screen """

        self.instructionsScreen = Interface_Frame(
            root, 0, 0, 1000, 600, "white")

        Interface_Label(root=self.instructionsScreen, path="src/images/frontend/Instructions/Instructions.png",
                               x_pos=450, y_pos=20, anchor=CENTER, bgColor="white", width=250, height=34)

        Interface_Label(root=self.instructionsScreen, path="src/images/frontend/Instructions/image 1.png",
                               x_pos=150, y_pos=110, anchor=CENTER, bgColor="white", width=100, height=54)

        Interface_Label(root=self.instructionsScreen, path="src/images/frontend/Instructions/image1Text.png",
                               x_pos=490, y_pos=110, anchor=CENTER, bgColor="white", width=450, height=45)

        Interface_Label(root=self.instructionsScreen, path="src/images/frontend/Instructions/image 2.png",
                               x_pos=150, y_pos=230, anchor=CENTER, bgColor="white", width=100, height=98)

        Interface_Label(root=self.instructionsScreen, path="src/images/frontend/Instructions/image2Text.png",
                               x_pos=490, y_pos=230, anchor=CENTER, bgColor="white", width=450, height=43)

        Interface_Label(root=self.instructionsScreen, path="src/images/frontend/Instructions/image 3.png",
                               x_pos=150, y_pos=350, anchor=CENTER, bgColor="white", width=100, height=98)

        Interface_Label(root=self.instructionsScreen, path="src/images/frontend/Instructions/image3Text.png",
                               x_pos=490, y_pos=350, anchor=CENTER, bgColor="white", width=450, height=25)

        Interface_Label(root=self.instructionsScreen, path="src/images/frontend/Instructions/image 4.png",
                               x_pos=150, y_pos=480, anchor=CENTER, bgColor="white", width=100, height=98)

        Interface_Label(root=self.instructionsScreen, path="src/images/frontend/Instructions/image4Text.png",
                               x_pos=490, y_pos=480, anchor=CENTER, bgColor="white", width=450, height=18)

        # Next Button
        Interface_Button(
            self.instructionsScreen, "src/images/frontend/Onboarding/Button.png", 150, 39, "white", FLAT, 450, 540, CENTER, lambda: DistanceScreen(Interface_Frame,root, Interface_Label=Interface_Label, window=camera))
