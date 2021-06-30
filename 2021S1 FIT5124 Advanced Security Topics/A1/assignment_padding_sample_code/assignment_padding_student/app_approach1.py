import utilities
import os
import operator

inverted_index_file = "inverted_index_5000"
frequency_file = "frequency_5000.csv"    

#read the dataset into a dictionary
inverted_dict = {}    
inverted_dict = utilities.read_dataset(inverted_index_file)

#Approach 1 : padding keywords such that
# they have the same result length as the most frequent keyword and then identify overhead .
# find the most frequency length & find the real amount of ids
longest = 0
for id_list in inverted_dict.values():
    if len(id_list) > longest:
        longest = len(id_list)
    
# append pid & count real & padding
count_real = 0
count_padding = 0
for id_list in inverted_dict.values():
    count_real += len(id_list)
    if len(id_list) < longest:
        diff = longest - len(id_list)
        for i in range(diff):
            # id_list.add(utilities.generate_random_id())
            # because the program runs so slow, we replace the generator with i. But in real case, we will use generate_random_id().
            id_list.add(i)
            count_padding += 1
            print("added!",count_padding)

# calculate overhead
pad_overhead = (count_real + count_padding) / count_real

print("Approach 1")
print("The count of padding is: " + str(count_padding))
print("The count of real pairs is: " + str(count_real))
print("The padding overhead is: " + str(pad_overhead))
        
# write the dic after padding to a new file
with open("map1.txt", "w", newline='') as writer:
    writer.write("Approach 1\n")
    writer.write("keyword, frequency\n")
    for keyword,id_list in inverted_dict.items():
        writer.write(keyword + "->" + str(len(id_list))+ "\n")
    writer.write("The count of padding is: " + str(count_padding) + "\n")
    writer.write("The count of real pairs is: " + str(count_real)+ "\n")
    writer.write("The padding overhead is: " + str(pad_overhead)+ "\n")
writer.close()