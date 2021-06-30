import random
import os
import operator
import csv
from itertools import cycle
import numpy as np
from scipy.optimize import linear_sum_assignment

#https://docs.scipy.org/doc/scipy-0.18.1/reference/generated/scipy.optimize.linear_sum_assignment.html

def cumulative_attack(raw_data,ope_data):

    #Step 1: compute the histograms of list_raw_data and ope_data
    raw_data_hist = {}
    ope_data_hist = {}
    histo(raw_data, raw_data_hist)
    histo(ope_data, ope_data_hist)
    
    #Step 2: compute emperical CDFs of raw and ope data
    raw_data_keys = sorted(list(raw_data_hist.keys()))
    ope_data_keys = sorted(list(ope_data_hist.keys()))
    
    raw_data_cdf = cdf_histo(raw_data_keys, raw_data_hist)
    ope_data_cdf = cdf_histo(ope_data_keys, ope_data_hist)
      
    #Step 3_1: Compute the cost matrix C and then use LSAP
    C =   [[] for _ in range(len(ope_data_keys))]
    
    for i in range(len(ope_data_keys)):
        for j in range(len(raw_data_keys)):
            C[i].append((abs(ope_data_hist[ope_data_keys[i]] - raw_data_hist[raw_data_keys[j]]))**2 + (abs(ope_data_cdf[ope_data_keys[i]] - raw_data_cdf[raw_data_keys[j]]))**2)

    #Step 3_2: apply linear_sum_assignment to identify the weight matrix X
    row_ind, col_ind = linear_sum_assignment(C) 

    #Step 4: export the mapping
    with open("map.txt", "w", newline='') as writer:
        writer.write("enc_age,raw_age\n")  
        for index in range(len(raw_data_keys)):
            writer.write(str(ope_data_keys[index]) + "->" + str(raw_data_keys[col_ind[index]])+ "\n")
    writer.close() 
    return 0

def file_reader (reader, lst,index):

    for i, row in enumerate(reader): #i starts from 0
        if i!=0:
            lst.append(int(row[index]))
            
def histo (list_data, dic):
    
    for item in list_data: #i starts from 0
        if item in dic:
            dic[item] += 1
        else:
            dic[item] =1

def cdf_histo (sorted_list_data, dic):
    
    new_dic = dic.copy()

    for index in range(len(sorted_list_data)):
        if index != 0:
            new_dic[sorted_list_data[index]] += new_dic[sorted_list_data[index-1]]
    return new_dic
  
if __name__ == '__main__':

    #raw dict and enc dict
    raw_age= list()
    enc_age = list()

    #read the plaintext  file
    plaintext_file = open("auxiliary.csv", "r", newline='') #   covid_true dataset.csv
    p_reader = csv.reader(plaintext_file,delimiter=',')
    file_reader(p_reader,raw_age,0)


    #read the cipher  file
    cipher_file = open("ope_enc_covid_age.csv", "r", newline='')
    c_reader = csv.reader(cipher_file,delimiter=',')
    file_reader(c_reader,enc_age,0)


    cumulative_attack(raw_age,enc_age) 


