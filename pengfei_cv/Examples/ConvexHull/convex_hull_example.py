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

input_image = "resources/world_map.jpg"

src = cv2.imread(input_image, cv2.IMREAD_UNCHANGED)
cv2.imshow("Source", src)

# convert image to gray scale
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
blur = cv2.blur(gray, (3, 3))
    
# binary thresholding of the image
_, thresh = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY)
    
# find contours
im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, \
        cv2.CHAIN_APPROX_SIMPLE)
    
# calculate points for each contour
hull = []
for i in range(len(contours)):
    hull.append(cv2.convexHull(contours[i], False))
    
# create an empty black image
drawing = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)
color_contours = (0, 255, 0)
color_convex_hull = (255, 255, 255)
   
for i in range(len(contours)):
    cv2.drawContours(drawing, contours, i, color_contours, 2, 8, hierarchy)
    cv2.drawContours(drawing, hull, i, color_convex_hull, 2, 8)

cv2.imshow("Output", drawing)
cv2.waitKey(0)
cv2.destroyAllWindows()