"""
Author: Pengfei Ren
Email: rpfly0818@gmail.com

╔┓┏╦━━╦┓╔┓╔━━╗
║┗┛║┗━╣┃║┃║oo║
║┏┓║┏━╣┗╣┗╣╰╯║
╚┛┗╩━━╩━╩━╩━━╝
"""

import cv2


def read_and_display_image(image_name, option=cv2.IMREAD_UNCHANGED):
    """
    Read and display a single image.

    parameters:
        image_name(string): The path of image file.
        option(int): The flag for specifying how the image should be read. Same options as 'cv2.imread'.

    returns:
        None
    """
    # Read image.
    img = cv2.imread(image_name, option)

    # Show image.
    cv2.imshow('Image Window', img)
    cv2.waitKey(0)

    cv2.destroyAllWindows()
