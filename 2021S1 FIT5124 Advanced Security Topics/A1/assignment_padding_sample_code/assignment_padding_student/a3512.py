import utilities
import os
import operator
import csv
from itertools import cycle


inverted_index_file = "inverted_index_5000"
frequency_file = "frequency_5000.csv"
id_list = list()
file = open(frequency_file, "r", newline='')
csv_reader = csv.reader(file,delimiter=',')
for i, row in enumerate(csv_reader): #i starts from 0
    id_list.append(int(row[1]))

print(id_list)
#read the dataset into a dictionary
inverted_dict = {}    
inverted_dict = utilities.read_dataset(inverted_index_file)


#Approach 3: given the keywords and clusters, perform padding and identify the padding overhead

#cluster size: 256
#cluster_points_256 = [0,392,648,904,1160,1416,1672,1928,2184,2440,2696,2952,3208,3464,3720,3976,4232,4488,4744,5000] # 1-392, 393-648, ... aka 0-391, 392-647, 648 - 903, ...
cluster_points_512 = [0,904,1416,1928,2440,2952,3464,3976,4488,5000]


count_padding = 0
count_real = 0
for id_set in inverted_dict.values():
    count_real += len(id_set)
    for i in range(len(cluster_points_512)-1):
        highest = id_list[cluster_points_512[i]]
        lowest = id_list[cluster_points_512[i+1]-1]
        if len(id_set) >= lowest and len(id_set) <= highest:
            diff = highest - len(id_set)
            if diff != 0:
                for k in range(diff):
                    id_set.add(k)
                    count_padding += 1
                    print("added!",count_padding)

    calculate overhead
pad_overhead = (count_real + count_padding) / count_real
print("Approach 3", 512)
print("The count of padding is: " + str(count_padding))
print("The count of real pairs is: " + str(count_real))
print("The padding overhead is: " + str(pad_overhead))


# write the dic after padding to a new file
with open("map3_512.txt", "w", newline='') as writer:
    writer.write("Approach 3 512\n")
    writer.write("keyword, frequency\n")
    for keyword,id_set in inverted_dict.items():
        writer.write(keyword + "->" + str(len(id_set))+ "\n")
    writer.write("The count of padding is: " + str(count_padding) + "\n")
    writer.write("The count of real pairs is: " + str(count_real)+ "\n")
    writer.write("The padding overhead is: " + str(pad_overhead)+ "\n")
writer.close()