"""
Author: Pengfei Ren
Email: rpfly0818@gmail.com

╔┓┏╦━━╦┓╔┓╔━━╗
║┗┛║┗━╣┃║┃║oo║
║┏┓║┏━╣┗╣┗╣╰╯║
╚┛┗╩━━╩━╩━╩━━╝
"""
import cv2


def build_video_writer(video_name, frame_width, frame_height, fps=10):
    """
    Build a video writer object.

    Parameters:
        video_name(string): The output video file name.
        frame_width(int): The width of frame in pixel.
        frame_height(int): The height of frame in pixel.
        fps(int): Frame rate.
    
    Returns:
        video_writer(cv2.VideoWriter): The video writer.
    """
    # Define the codec and create VideoWriter object.
    out = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc('M','J','P','G'), fps, (frame_width,frame_height))
