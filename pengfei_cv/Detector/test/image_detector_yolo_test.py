"""
Author: Pengfei Ren
Email: rpfly0818@gmail.com

╔┓┏╦━━╦┓╔┓╔━━╗
║┗┛║┗━╣┃║┃║oo║
║┏┓║┏━╣┗╣┗╣╰╯║
╚┛┗╩━━╩━╩━╩━━╝
"""

import cv2
import context
import downloader
import image_detector_yolo

model_configuration = "resources/yolov3.cfg"
model_weights = "resources/yolov3.weights"
classes_file = "resources/coco.names"

model_files = {
    model_configuration: "https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg?raw=true",
    model_weights: "https://pjreddie.com/media/files/yolov3.weights",
    classes_file: "https://github.com/pjreddie/darknet/blob/master/data/coco.names?raw=true"}

# downloader.download_files(model_files)

yolo_detector = image_detector_yolo.load_yolo_model(model_configuration, model_weights)

image_name = "resources/bird.jpg"

      
classes = None
with open(classes_file, 'rt') as f:
    classes = f.read().rstrip('\n').split('\n')

img = cv2.imread(image_name)

# Network input dimensions
input_height = 416
input_width = 416
    
# Create a 4D batch from a img.
batch = cv2.dnn.blobFromImage(img, 1/255, (input_width, input_height), 
                              [0,0,0], 1, crop=False)
yolo_detector.setInput(batch)

outs = yolo_detector.forward(
    image_detector_yolo.get_outputs_names(yolo_detector))

# Remove the bounding boxes with low confidence
image_detector_yolo.post_process(img, outs, classes)

# Put efficiency information. 
# getPerfProfile returns the overall time for inference(t) and 
# the timings for each of the layers(in layersTimes)
t, _ = yolo_detector.getPerfProfile()
label = 'Inference time: %.2f ms' % (t * 1000.0 / cv2.getTickFrequency())

cv2.putText(img, label, (0, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))

cv2.imwrite("resources/yolo.jpg", img)