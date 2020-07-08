# Data Cleaner file.
# I got the list of wards in Bangalore from Wikipedia. This list is stored in 'input_data.txt'
# This file write the name of the wards in 'ward_list.txt' file for each input line.


f = open("input_data.txt","r")
f1 = open("ward_list.txt", "w+")
for i in range(198):
	array = f.readline().split(" ")
	array_ = array[0].split("\t")
	#print(array)
	f1.write(array_[1] + "\n")

f.close()
f1.close()