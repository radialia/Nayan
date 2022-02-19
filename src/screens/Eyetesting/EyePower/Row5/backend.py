from tkinter import *

def results(root, Interface_Frame, Interface_Label):
    eyePowerScreen = Interface_Frame(
            root, 0, 0, 1000, 600, "white")

    Interface_Label(eyePowerScreen, "src/images/frontend/Results/Subheading.png", 450, 50, CENTER, "white", 200, 16)
    Interface_Label(eyePowerScreen, "src/images/frontend/Results/20by40.png", 450, 140, CENTER, "white", 272, 108)

    Interface_Label(eyePowerScreen, "src/images/frontend/Results/Title1.png",60, 240, CENTER, "white", 100, 21)
    Interface_Label(eyePowerScreen, "src/images/frontend/Results/Description.png",210, 300, CENTER, "white", 400, 60)
    Interface_Label(eyePowerScreen, "src/images/frontend/Results/Description1.png",210, 380, CENTER, "white", 400, 60)

    Interface_Label(eyePowerScreen, "src/images/frontend/Results/Title2.png",580, 240, CENTER, "white", 180, 26)
    Interface_Label(eyePowerScreen, "src/images/frontend/Results/Description2.png",680, 310, CENTER, "white", 400, 86)