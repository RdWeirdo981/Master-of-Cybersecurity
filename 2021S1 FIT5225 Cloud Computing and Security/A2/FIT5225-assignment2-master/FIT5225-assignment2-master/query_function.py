import json
import boto3
from boto3.dynamodb.conditions import Attr

def lambda_handler(event,context):
    if event:
        
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('ObjectDetection_Table')
        
        # get all tags and put that into a list for further processing
        key_list = []
        print(type(event))
        for key in event:
            if event[key] != '':
                key_list.append(event[key])
        
        # url_set is the set for collecting all urls 
        url_set = set()
        # url_list is the set for collecting all urls 
        url_list = []
        # final_url_list is the set for collecting all urls 
        final_url_list = []
        
        # gets the maximum number of objects in the table
        resp1 = table.scan()                            #
        var_len = 0                                     #
        for each in resp1['Items']:                     #
            if var_len >= len(each):                    #
                continue                                #
            elif var_len < len(each):                   #
                var_len = len(each)                     #
        # gets the maximum number of objects in the table
                
        #gets the url of the all the objects sepecified by the user #############################
        for obj in key_list:                                                                    #
            for i in range(1, var_len):                                                         #
                resp = table.scan(FilterExpression=Attr('Object'+str(i)).eq(obj))               # 
                
                if resp['Items'] != []:                                                         #
                    for each in resp['Items']:                                                  #
                        url_list.append(each["url"])                                            #
                        url_set.add(each["url"])
        
        for each1 in url_set:                                                                   #
            if url_list.count(each1) == len(key_list):                                          #                                                    # 
                final_url_list.append(each1)                                                    #
            
        #gets the url of the all the objects sepecified by the user #############################
            
        return {'links': list(final_url_list)}
 
