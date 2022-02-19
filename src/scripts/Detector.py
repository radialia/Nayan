# Importing all the modules
import cv2 as vision
import mediapipe as mp

# Face detector class for mediapipe with 60% confidence and model selcted 1 for distant recognition
face_detection = mp.solutions.face_detection.FaceDetection(
    min_detection_confidence=0.5, model_selection=1)


def face_detector(frame):
    """
        This function is used to detect the face from the web cam of the laptop/ mobile
        This function also returns the face width of the user according to the size of the image

        :param (frame): Takes in the frame or image for the face detection
        :return (config, confidence): Returns the configurations of the detected face(x, y, w, h) and the confidence
    """
    # Initialisation of default value
    configuration = 0

    # Converting from BGR to RGB
    frame = vision.cvtColor(frame, vision.COLOR_BGR2RGB)
    # Changed access to unwrite for more accuracy
    frame.flags.writeable = False
    # Face detection through mediapipe
    results = face_detection.process(frame)

    # Reverting back all the changes
    frame.flags.writeable = True
    frame = vision.cvtColor(frame, vision.COLOR_RGB2BGR)

    # If the results.detections is not empty
    if results.detections:
        # loop through it
        for detection in results.detections:

            # Get the bounding box configuration
            bounding_box = detection.location_data.relative_bounding_box

            # Get the height, width of the frame
            height, width, channel = frame.shape

            # Calculate the configurations
            configuration = int(bounding_box.xmin * width), int(bounding_box.ymin * height), \
                int(bounding_box.width * width), int(bounding_box.height * height)

    # Return values
    return configuration
