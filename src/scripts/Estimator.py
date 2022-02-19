def focal_length_calculator(width_in_image, distance_in_image, real_width_of_object):
    """
    This function is used to calculate the focal length for the distnace estimation
    using triangle similarity

    :param1 (width_in_image): The width of the object in the reference image
    :param2 (distance_in_image): The distance of the object from the screen [measured] in the reference image
    :param3 (real_width_of_object): The real width of the object [measured] in the reference image

    :returns (focal_length): The focal_length is the product of all the parameters
    """
    return ((width_in_image * distance_in_image)/real_width_of_object)


def distance_calculator(focal_length, real_width_of_object, width_in_frame):
    """
    This function is used to calculate the estimated distnace using
    triangle similarity

    :param1 (focal_length): The focal_length in the reference image as calculated
    :param2 (real_width_of_object): The real width of the object [measured] in the reference image
    :param3 (width_in_frame): The width of the object in frame

    :returns (distance): The distance is the return
    """
    return ((focal_length * real_width_of_object)/width_in_frame)
