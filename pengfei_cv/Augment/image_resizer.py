"""
Author: Pengfei Ren
Email: rpfly0818@gmail.com

╔┓┏╦━━╦┓╔┓╔━━╗
║┗┛║┗━╣┃║┃║oo║
║┏┓║┏━╣┗╣┗╣╰╯║
╚┛┗╩━━╩━╩━╩━━╝
"""

import cv2
import numpy as np


def scale_image(image, scale_factor):
    """
    Resize image with given scale_factor. 

    Parameters:
        image(np.array): image read with cv2.
        scale_factor(float): scale factor.
    
    Returns:
        image(np.array): resized image.
    """
    h = np.ceil(image.shape[0] * scale_factor).astype(int)
    w = np.ceil(image.shape[1] * scale_factor).astype(int)

    image = cv2.resize(image, (w, h))

    return image


def crop_image(image, crop_box):
    """
    Crop image with given crop box.

    Parameters:
        image(np.array): image to be cropped.
        crop_box(numpy_array): [xmin, ymin, w, h]
    
    Returns:
        image(np.array): cropped image.
    """
    # NOTE: x and y are flipped.
    return image[crop_box[1]: crop_box[1] + crop_box[3], 
                 crop_box[0]: crop_box[0] + crop_box[2]]