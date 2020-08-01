"""
Author: Pengfei Ren
Email: rpfly0818@gmail.com

╔┓┏╦━━╦┓╔┓╔━━╗
║┗┛║┗━╣┃║┃║oo║
║┏┓║┏━╣┗╣┗╣╰╯║
╚┛┗╩━━╩━╩━╩━━╝
"""

import cv2


def render_bbox_2d(image, bbox_2d, color=(0, 0, 255), line=2):
    """
    Render 2D bounding box on given image.

    Parameters:
        image (numpy.array): Image in opencv format.
        bbox_2d (numpy.array): Corners of 2D bounding box of shape [xmin, ymin, xmax, ymax]

    Returns:
        image (numpy.array): Image with bbox drawn.
    """
    left_up = (bbox_2d[0], bbox_2d[1])
    right_bottom = (bbox_2d[2], bbox_2d[3])

    image = cv2.rectangle(image, left_up, right_bottom, color, line)

    return image
