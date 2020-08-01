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


def load_yolo_model(model_configuration, model_weights, processor=cv2.dnn.DNN_TARGET_CPU):
    """
    Load YOLO configurations and model weights.

    Parameters:
        model_configuration(string): Model configuration file.
        model_weights(string): Model parameter weights file.
        processor(int): Processor option for running the neural network. Use `DNN_TARGET_CUDA`
        for nVidia GPU.
    
    Returns:
        yolo: yolo detector.
    """

    yolo = cv2.dnn.readNetFromDarknet(model_configuration, model_weights)
    yolo.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
    yolo.setPreferableTarget(processor)

    return yolo

def get_outputs_names(model):
    """
    Get the names of the output layers

    Parameters:
        mode: Neural network model.
    
    Returns:
        A list of output layer names.
    """
    # Get the names of all the layers in the network
    layersNames = model.getLayerNames()

    # Get the names of the output layers, i.e. the layers with unconnected outputs
    return [layersNames[i[0] - 1] for i in model.getUnconnectedOutLayers()]


def draw_pred(image, classes, classId, conf, left, top, right, bottom):
    """
    Draw the predicted bounding box.

    Parameters:
        image(np.array): Input image.
        classes(list): A list of classes names.
        conf(float): Confidence score.
        left(int): Left boundary of box.
        top(int): Top boundary of box.
        right(int): Right boundary of box.
        Bottom(int): Bottom boundary of box.

    Returns:
        image
    """
    # Draw a bounding box.
    cv2.rectangle(image, (left, top), (right, bottom), (255, 178, 50), 3)
    
    label = '%.2f' % conf
        
    # Get the label for the class name and its confidence
    if classes:
        assert(classId < len(classes))
        label = '%s:%s' % (classes[classId], label)

    #Display the label at the top of the bounding box
    labelSize, baseLine = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
    top = max(top, labelSize[1])

    cv2.rectangle(image, (left, top - round(1.5*labelSize[1])), 
        (left + round(1.5*labelSize[0]), top + baseLine), (255, 255, 255), cv2.FILLED)
    cv2.putText(image, label, (left, top), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,0), 1)

    return image

def post_process(image, outs, classes, confidence_threshold=0.5, nms_threshold=0.4):
    """
    Remove the bounding boxes with low confidence using NMS, and draw bounding box.

    Parameters:
        image(np.array): Network input image.
        outputs(np.array): Network outputs.
    """
    image_height = image.shape[0]
    image_width = image.shape[1]

    classIds = []
    confidences = []
    boxes = []

    # Scan through all the bounding boxes output from the network 
    # and keep only the ones with high confidence scores. 
    # Assign the box's class label as the class with the highest score.
    classIds = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            classId = np.argmax(scores)
            confidence = scores[classId]
            if confidence > confidence_threshold:
                center_x = int(detection[0] * image_width)
                center_y = int(detection[1] * image_height)
                width = int(detection[2] * image_width)
                height = int(detection[3] * image_height)
                left = int(center_x - width / 2)
                top = int(center_y - height / 2)
                classIds.append(classId)
                confidences.append(float(confidence))
                boxes.append([left, top, width, height])

    # Perform non maximum suppression to eliminate redundant overlapping boxes with
    # lower confidences.
    indices = cv2.dnn.NMSBoxes(boxes, confidences, confidence_threshold, nms_threshold)
    for i in indices:
        i = i[0]
        box = boxes[i]
        left = box[0]
        top = box[1]
        width = box[2]
        height = box[3]
        draw_pred(image, classes, classIds[i], confidences[i], left, top, left + width, top + height)
    
    return image

