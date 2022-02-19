from tkinter import *

class DistanceScreen:
    def __init__(self,Interface_Frame, root, window, Interface_Label):
        """ Distance Estimator Screen """
        self.distanceScreen = Interface_Frame(
            root, 0, 0, 1000, 600, "white")
        window.startCamera()

        Interface_Label(
        self.distanceScreen, "src/images/frontend/User Authentication/Instructions.png", 450, 540, CENTER, "white", 500, 76)
        
        