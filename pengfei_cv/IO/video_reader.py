"""
Author: Pengfei Ren
Email: rpfly0818@gmail.com

╔┓┏╦━━╦┓╔┓╔━━╗
║┗┛║┗━╣┃║┃║oo║
║┏┓║┏━╣┗╣┗╣╰╯║
╚┛┗╩━━╩━╩━╩━━╝
"""
import cv2


def read_and_display_video(video_name):
    """
    Read and display video file. Press 'q' to exit video play.

    Parameters:
        video_name(string): The path of video file.
    
    Returns:
        None
    """

    # Create a VideoCapture object and read from input file
    cap = cv2.VideoCapture(video_name)

    if (cap.isOpened()== False): 
      print("Error opening video stream or file")

    while(cap.isOpened()):
      ret, frame = cap.read()
      if ret == True:
        cv2.imshow('Video Window',frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
          break
      else: 
        break

    # When everything done, release the video capture object
    cap.release()
    cv2.destroyAllWindows()
