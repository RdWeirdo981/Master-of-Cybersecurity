import boto3
import cv2
import os
import numpy as np
# from numpy import argmax
#from werkzeug.utils import secure_filename
import json

coco_names = ['person', 'bicycle', 'car', 'motorbike', 'aeroplane', 'bus', 'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'sofa', 'pottedplant', 'bed', 'diningtable', 'toilet', 'tvmonitor', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush']

def lambda_handler(event,context):
    
    if event:
        
        s3 = boto3.client("s3")
        
        dynamoDB = boto3.client('dynamodb')
        
        table_name = 'ObjectDetection_Table'
        
        # Fetching image filename from s3 bucket ############
        print("Event: ", event)                             #
        file_obj = event["Records"][0]                      #
        filename = str(file_obj['s3']['object']['key'])     #
        print('filename: ',filename)                        #
        #####################################################
        
        # Get url from of the images from the s3 bucket ########################################################################
        s3_url = s3.generate_presigned_url('get_object', Params = {'Bucket': 'object-detection-image-dump', 'Key': filename})  #
        s3_url_test= (s3_url.split("?"))                                                                                       #
        print(s3_url_test)                                                                                                     #
        ########################################################################################################################
        
        # converts the image file to numpy array ##########################################
        fileObj = s3.get_object(Bucket = "object-detection-image-dump", Key=filename)     #
        file_content = fileObj["Body"].read()                                             #
        np_array = np.fromstring(file_content,np.uint8)                                   #
        image_np = cv2.imdecode(np_array, cv2.IMREAD_COLOR)                               #
        print("Type is: ",type(image_np))                                                 #
        ###################################################################################
        
        # Loads the Yolo algorithm
        net_obj = cv2.dnn.readNet('/opt/yolov3-tiny.weights', '/opt/yolov3-tiny.cfg')
        
        # Object detection block ####################################################################
        class_ids = []                                                                              #
        accuracy = []                                                                               #
         
        lnames = net_obj.getLayerNames()                                                            #
        layers = [lnames[i[0] - 1] for i in net_obj.getUnconnectedOutLayers()]                      #
        
        blob = cv2.dnn.blobFromImage(image_np, 0.00392, (320, 320), (0, 0, 0), True, crop=False)    # 
            
        net_obj.setInput(blob)                                                                      #
        
        result_det = net_obj.forward(layers)                                                        #
    
        for each_result in result_det:                                                              #
            for each in each_result:                                                                #
                scores = each[5:]                                                                   #
                class_id = np.argmax(scores)                                                        #
                confidence = scores[class_id]                                                       #
                if confidence > 0.5:                                                                #
                    accuracy.append(float(confidence))                                              #
                    class_ids.append(class_id)                                                      #
        #############################################################################################        
    
        # Convert the object list to set to get unique object values ##
        objects = set()                                               #
        length = len(class_ids)                                       #
        for i in range(length):                                       #
            objects.add(str(coco_names[class_ids[i]]))                #
        ###############################################################
       
        # Put the detected objects to the DynamoDB ###########################
        data = {}                                                            #
        data['url'] = {'S': s3_url_test[0]}                                 #
       
        i = 1                                                                #
        for each in objects: 
            print(each)                                                      #
            data["Object"+str(i)]= {'S': each}                               #
            print(data)                                                      #
            i=i+1                                                            # 
            print(i)                                                         #
           
        response = dynamoDB.put_item(TableName=table_name,Item=data)         #
        ######################################################################
