
import utilities
import os
import operator

inverted_index_file = "inverted_index_5000"
frequency_file = "frequency_5000.csv"    

#read the dataset into a dictionary
inverted_dict = {}    
inverted_dict = utilities.read_dataset(inverted_index_file)

#Approach 2: padding the keywords to the multiplication of an integer 100 and identify padding overhead

# select multiplication
n = 100
# append pid to the nearest multiplication of 5 & count padding
count_real = 0
count_padding = 0
for id_list in inverted_dict.values():
    count_real += len(id_list)
    i = 1
    while (len(id_list) > i * n):
        i += 1 # find the nearest 5i larger than len(id_list)
    if len(id_list) < i*n:
        diff = i*n - len(id_list)
        for i in range(diff):
            if i in id_list:
                id_list.add(utilities.generate_random_id)
            else:
                id_list.add(i)
            count_padding += 1
            print("added!",count_padding)
# calculate overhead
pad_overhead = (count_real + count_padding) / count_real

print("Approach 2")
print("The count of padding is: " + str(count_padding))
print("The count of real pairs is: " + str(count_real))
print("The padding overhead is: " + str(pad_overhead))
        
# write the dic after padding to a new file
with open("map2.txt", "w", newline='') as writer:
    writer.write("Approach 2\n")
    writer.write("keyword, frequency\n")
    for keyword,id_list in inverted_dict.items():
        writer.write(keyword + "->" + str(len(id_list))+ "\n")
    writer.write("The count of padding is: " + str(count_padding) + "\n")
    writer.write("The count of real pairs is: " + str(count_real)+ "\n")
    writer.write("The padding overhead is: " + str(pad_overhead)+ "\n")
writer.close()