# Generate the parallel requests based on the ThreadPool Executor
from concurrent.futures import ThreadPoolExecutor as PoolExecutor
import sys
import time
import glob
import requests
import threading
import uuid
import base64
import json
import os

#send http request
def call_object_detection_service(image):
    try:

        url = "http://118.138.245.115:80/server"
        data = {}
        #generate uuid for image
        id =   uuid.uuid5(uuid.NAMESPACE_OID, image)
        # Encode image into base64 string
        with open (image, 'rb') as image_file:
            data['image'] =  base64.b64encode(image_file.read()).decode('utf-8')

        data ['id'] = str(id)

        headers = {'Content-Type': 'application/json'}

        response = requests.post(url, json = json.dumps(data), headers = headers)

        if response.ok:
            output = "Thread : {},  input image: {},  output:{}".format(threading.current_thread().getName(),
                                                                        image,  response.text)
            print(output)
        else:
            print ("Error, response status:{}".format(response))

    except Exception as e:
        print("Exception in webservice call: {}".format(e))

# gets list of all images path from the input folder
def get_images_to_be_processed(input_folder):
    images = []
    for image_file in glob.iglob(input_folder + "*.jpg"):
        images.append(image_file)
    return images

def main():
    ## provide argumetns-> input folder, url, number of wrokers

    path = "inputfolder/"
    images = get_images_to_be_processed(path)
    num_images = images.__len__()

    thread_list = [1,6,11,16,21,26,31]
    response_time = []
    for thread in thread_list:
        for _ in range(3):
            start_time = time.time()
            #craete a worker  thread  to  invoke the requests in parallel
            with PoolExecutor(max_workers=thread) as executor:
                for _ in executor.map(call_object_detection_service,  images):
                    pass
            elapsed_time =  time.time() - start_time
            response_time.append("Thread {}: Total time spent: {}, average response time: {} ".format(thread,elapsed_time, elapsed_time/num_images))
    for item in response_time:
        print(item)

if __name__ == "__main__":
    main()


