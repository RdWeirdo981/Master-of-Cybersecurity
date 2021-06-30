import os, csv, pickle
import random
import json
import numpy as np
import operator

max_bogus_size_document = 550000

def read_dataset(inverted_index_file):

    #read the dataset into a dictionary
    inverted_dict = {}    
    f1 = open(inverted_index_file, "rb") 
    inverted_dict = pickle.load(f1)
    f1.close()

    #brief report about the dataset
    print("Dataset information")

    counter = 0
    total_pairs = 0
    for keyword,id_list in inverted_dict.items():
        counter +=1
        total_pairs +=len(id_list)
    
    print("total no. of keywords: " + str(counter))
    print("database size: the number of (keyword,id) pairs: " + str(total_pairs))

    return inverted_dict

def identify_keywords_frequencies(inverted_dict):

    #read keyword frequency from the index
    dict_frequency = {}
    for keyword in inverted_dict:
        dict_frequency[keyword] =len(inverted_dict[keyword])

    #sorted keywords by descending order of frequencies
    sorted_dict_frequency = sorted(dict_frequency.items(), key=operator.itemgetter(1),reverse=True)      
    

def generate_random_id():
    file_count = [(100000 + i) for i in range(1,550000)]
    return random.choice(file_count)   
