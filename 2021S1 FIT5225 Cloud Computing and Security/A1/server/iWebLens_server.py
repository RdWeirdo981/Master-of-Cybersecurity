# import the necessary packages
import numpy as np
import time
import cv2
import os
import json
from flask import Flask, request, jsonify
import base64

# construct the argument parse and parse the arguments
confthres = 0.3
nmsthres = 0.1


def get_labels(labels_path):
    # load the COCO class labels our YOLO model was trained on
    lpath = os.path.sep.join([yolo_path, labels_path])

    print(yolo_path)
    LABELS = open(lpath).read().strip().split("\n")
    return LABELS


def get_weights(weights_path):
    # derive the paths to the YOLO weights and model configuration
    weightsPath = os.path.sep.join([yolo_path, weights_path])
    return weightsPath


def get_config(config_path):
    configPath = os.path.sep.join([yolo_path, config_path])
    return configPath


def load_model(configpath, weightspath):
    # load our YOLO object detector trained on COCO dataset (80 classes)
    print("[INFO] loading YOLO from disk...")
    net = cv2.dnn.readNetFromDarknet(configpath, weightspath)
    return net


def do_prediction(image, net, LABELS):
    (H, W) = image.shape[:2]
    # determine only the *output* layer names that we need from YOLO
    ln = net.getLayerNames()
    ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    # construct a blob from the input image and then perform a forward
    # pass of the YOLO object detector, giving us our bounding boxes and
    # associated probabilities
    blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416),
                                 swapRB=True, crop=False)
    net.setInput(blob)
    start = time.time()
    layerOutputs = net.forward(ln)
    # print(layerOutputs)
    end = time.time()

    # show timing information on YOLO
    print("[INFO] YOLO took {:.6f} seconds".format(end - start))

    # initialize our lists of detected bounding boxes, confidences, and
    # class IDs, respectively
    boxes = []
    confidences = []
    classIDs = []

    # loop over each of the layer outputs
    for output in layerOutputs:
        # loop over each of the detections
        for detection in output:
            # extract the class ID and confidence (i.e., probability) of
            # the current object detection
            scores = detection[5:]
            # print(scores)
            classID = np.argmax(scores)
            # print(classID)
            confidence = scores[classID]

            # filter out weak predictions by ensuring the detected
            # probability is greater than the minimum probability
            if confidence > confthres:
                # scale the bounding box coordinates back relative to the
                # size of the image, keeping in mind that YOLO actually
                # returns the center (x, y)-coordinates of the bounding
                # box followed by the boxes' width and height
                box = detection[0:4] * np.array([W, H, W, H])
                (centerX, centerY, width, height) = box.astype("int")

                # use the center (x, y)-coordinates to derive the top and
                # and left corner of the bounding box
                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))

                # update our list of bounding box coordinates, confidences,
                # and class IDs
                boxes.append([x, y, int(width), int(height)])

                confidences.append(float(confidence))
                classIDs.append(classID)

    # apply non-maxima suppression to suppress weak, overlapping bounding boxes
    idxs = cv2.dnn.NMSBoxes(boxes, confidences, confthres,
                            nmsthres)

    # TODO Prepare the output as required to the assignment specification
    # ensure at least one detection exists

    response_dict = {}  # empty dict for "objects": [{item1}, {item2}, ...]
    response_list = []

    if len(idxs) > 0:
        # loop over the indexes we are keeping
        for i in idxs.flatten():
            item_dict = {}  # empty dict for label, accuracy, rectangle
            rectangle_dict = {}

            item_dict["label"] = LABELS[classIDs[i]]
            item_dict["accuracy"] = confidences[i]
            rectangle_dict["height"] = boxes[i][3]
            rectangle_dict["left"] = boxes[i][0]
            rectangle_dict["top"] = boxes[i][1]
            rectangle_dict["width"] = boxes[i][2]
            item_dict["rectangle"] = rectangle_dict

            response_list.append(item_dict)

    response_dict["objects"] = response_list
    return response_dict  # return a dict

## Yolov3-tiny versrion
yolo_path = "yolo_tiny_configs/"
labelsPath = "coco.names"
cfgpath = "yolov3-tiny.cfg"
wpath = "yolov3-tiny.weights"

Lables = get_labels(labelsPath)
CFG = get_config(cfgpath)
Weights = get_weights(wpath)


# TODO, you should  make this console script into webservice using Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return ("hello!")

@app.route('/server', methods = ['POST'])
def main():
    try:
        imagefile = request.get_data().decode()
        imagefile = json.loads(json.loads(imagefile))  # imagefile now is a dict: {'id':xxxx, 'image': yyyy}
        return_dict = {}  # this dict will be: {'id':xxxx, 'objects': [] }

        ## get reqest id
        return_dict['id'] = imagefile['id']

        ## get objects

        ## Decode base64
        decode_img = base64.b64decode(imagefile['image'])
        nparr = np.fromstring(decode_img, np.uint8)
        image = cv2.imdecode(nparr, cv2.COLOR_BGR2GRAY)

        # load the neural net.  Should be local to this method as its multi-threaded endpoint
        nets = load_model(CFG, Weights)
        object_dict = do_prediction(image, nets, Lables)
        return_dict['objects'] = object_dict['objects']

        ## jsonfy return_dict
        return jsonify(return_dict)

    except Exception as e:
        print("Exception  {}".format(e))
        return jsonify({'objects': 'invalid'})


if __name__ == '__main__':
    app.run(debug=True, threaded = True, host = '0.0.0.0')