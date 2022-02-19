from tkinter import *
from PIL import ImageTk, Image
from src.scripts.resourceLoader import resource_path
from cv2 import *
from tkinter import messagebox
from src.scripts.Detector import face_detector
from src.scripts.Estimator import focal_length_calculator, distance_calculator
from src.screens.Eyetesting.EyePower.Row1.frontend import Row1
from random import randint


class UserInterface:
    def __init__(self, video_source=0):
        """ Initializes and creates the main source """
        self.video_source = video_source
        self.count = 1

        # Array of hex codes for colors
        self.COLORS = [
            (34, 126, 230),
            (111, 220, 247),
            (128, 190, 82),
            (226, 173, 93)
        ]

        # Get a random color
        self.color = self.COLORS[randint(0, (self.COLORS.__len__() - 1))]

        # Known parameters for triangle similarity
        self.Known_Distance_From_Camera = 75
        self.Known_Width_Of_Face = 14

        self.root = Tk()

        self.title = "Nayan"
        self.root.title(self.title)

        self.root.geometry("900x600+225+50")
        self.root.iconphoto(False, PhotoImage(
            file=resource_path("src/images/frontend/Icon.png")))
        self.root.config(bg="white")

        self.root.resizable(0, 0)

    def startCamera(self):
        """ Initialize the camera source """
        self.camera = Camera(self.video_source)

        # Create a canvas to display video
        self.canvas = Canvas(
            self.root, width=self.camera.width, height=self.camera.height)
        self.canvas.place(x=450, y=250, anchor=CENTER)

        # Updation of the delay
        self.delay = 15
        self.update()

    def update(self):
        """ Get a frame from the video source and place it in the canvas created """
        _, frame = self.camera.readCamera()

        # Increment count
        self.count += 1

        # Get the configurations of face in the frame and reference image
        self.frame_config = face_detector(frame)
        self.image_config = face_detector(
            imread(resource_path("src/images/reference.jpg")))

        if(self.frame_config and self.image_config):
            # Get focal length
            self.focal_length = focal_length_calculator(
                self.image_config[2], self.Known_Distance_From_Camera, self.Known_Width_Of_Face)

            # Get distance
            self.distance = distance_calculator(
                self.focal_length, self.Known_Width_Of_Face, self.frame_config[2])

            # Draw a rectangle around the face
            rectangle(frame, (self.frame_config[0], self.frame_config[1]), (
                self.frame_config[0]+self.frame_config[2], self.frame_config[1]+self.frame_config[3]), self.color, 3)

            # Put distance text on the screen
            putText(frame, f"Distance: {round(self.distance,2)} cm", (
                self.frame_config[0] + 5, self.frame_config[1] - 15), FONT_HERSHEY_SIMPLEX, 0.60, self.color, 1)

            # Put instructions on screen
            if(self.distance < 110):
                putText(frame, f"Please move away from the screen",
                        (30, 35), FONT_HERSHEY_SIMPLEX, 1.0, self.color, 2)
            elif(self.distance > 110 and self.distance < 120):
                putText(frame, f"Screen distance is all perfect",
                        (30, 35), FONT_HERSHEY_SIMPLEX, 1.0, self.color, 2)
            else:
                putText(frame, f"Please come closer to the screen",
                        (30, 35), FONT_HERSHEY_SIMPLEX, 1.0, self.color, 2)

        if(self.count < 200):
            if _:
                # Show the video on the canvas
                self.photo = ImageTk.PhotoImage(
                    image=Image.fromarray(frame))
                self.canvas.create_image(0, 0, image=self.photo, anchor=NW)
                self.root.after(self.delay, self.update)
        else:
            self.camera.stopCamera()
            Row1(self.root,self.Interface_Frame,self.Interface_Label, self.Interface_Button)
            

    def Interface_Label(self, root, path, x_pos, y_pos, anchor, bgColor, width, height):
        """ Creates an image label on the screen """

        baseURL = Image.open(resource_path(path))
        resize_image = baseURL.resize((width, height))
        image = ImageTk.PhotoImage(resize_image)

        imageLabel = Label(root, image=image, bg=bgColor)
        imageLabel.image = image
        imageLabel.place(x=x_pos, y=y_pos, anchor=anchor)

    def Interface_Frame(self, root, x_pos, y_pos, width, height, bgColor):
        """ Creates a new frame on the current window """
        screen = Frame(root, width=width, height=height)
        screen.config(bg=bgColor)
        screen.place(x=x_pos, y=y_pos)

        return screen

    def Interface_Input(self, root, bgColor, thickness, width, relief, fontFamily, fontSize, fontStyle, background, color, x_pos, y_pos, height, show):
        """ Create an Input box on the screen """
        if(show):
            inputBox = Entry(root, background=bgColor, highlightthickness=thickness,
                             width=width, relief=relief, font=(fontFamily, fontSize, fontStyle), show=show)
        else:
            inputBox = Entry(root, background=bgColor, highlightthickness=thickness,
                             width=width, relief=relief, font=(fontFamily, fontSize, fontStyle))

        inputBox.config(highlightbackground=background, highlightcolor=color)
        inputBox.place(x=x_pos, y=y_pos, height=height)

        return inputBox

    def Interface_Button(self, root, path, width, height, bgColor, relief, x_pos, y_pos, anchor, command):
        """ Creates a button with an image """
        base_button = Image.open(resource_path(path))
        resize_button = base_button.resize((width, height))
        buttonImg = ImageTk.PhotoImage(resize_button)
        button = Button(root, image=buttonImg, bg=bgColor,
                        relief=relief, command=command, highlightthickness=0, bd=0)

        button.image = buttonImg
        button.place(x=x_pos, y=y_pos, anchor=anchor)

    def run(self):
        """ Runs the Tkinter GUI App """
        self.root.mainloop()


class Camera:
    def __init__(self, video_source=0):
        """ Open the camera and start recrding """
        self.video = VideoCapture(video_source, CAP_DSHOW)

        # Get video source width and height
        self.width = self.video.get(CAP_PROP_FRAME_WIDTH)
        self.height = self.video.get(CAP_PROP_FRAME_HEIGHT)

    def readCamera(self):
        """ Read each frames from the camera feed """
        _, frame = self.video.read()
        if _:
            return (_, flip(cvtColor(frame, COLOR_BGR2RGB), 1))
        else:
            return (_, None)

    def stopCamera(self):
        """ Release the camera """
        self.video.release()
        messagebox.showinfo("Success", "Distance Estimation process completed")
