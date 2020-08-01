"""
Author: Pengfei Ren
Email: rpfly0818@gmail.com

╔┓┏╦━━╦┓╔┓╔━━╗
║┗┛║┗━╣┃║┃║oo║
║┏┓║┏━╣┗╣┗╣╰╯║
╚┛┗╩━━╩━╩━╩━━╝
"""
import context
import cv2

# Create a VideoCapture object
cap = cv2.VideoCapture(0)

if (cap.isOpened() == False): 
  print("Unable to read camera feed")

# Default resolutions of the frame are obtained.
# Note: the default resolutions are system dependent.
# We convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

video_writer = build_video_writer('my_video.avi', frame_width, frame_height)

while(True):
  ret, frame = cap.read()
  if ret == True: 
    video_writer.write(frame)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  else:
    break  

cap.release()
video_writer.release()
cv2.destroyAllWindows() 
