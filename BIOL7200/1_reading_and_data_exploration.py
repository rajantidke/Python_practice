#!/usr/bin/env python

#Reading and writing files
my_file = open("plantgrowth.txt")
# print(type(my_file))
# <class '_io.TextIOWrapper'>

contents = my_file.read()
# print(contents)
# weight  group
# 4.17    ctrl
# 5.58    ctrl
# 5.18    ctrl
# 6.11    ctrl

# print(type(contents))
# <class 'str'>

bits = contents.split("\t")     #Since the data in the file was tab separated, this helps us explore the data in bits and pieces
#Exploring the first 5 elements is a standard practise in data exploratioon, hence we check 0:5 index slice  
# print(bits[:5])                 #Upto but not including index 5 in the bits list
bits[:5]
# ['weight', 'group\n4.17', 'ctrl\n5.58', 'ctrl\n5.18', 'ctrl\n6.11']                #Not very sensible choice of delimiter

bits = contents.split("\n")
# print(bits[:5])
bits[:5]                  
# ['weight\tgroup', '4.17\tctrl', '5.58\tctrl', '5.18\tctrl', '6.11\tctrl']          #Slightly better as every element is a row from the data file

# print(bits[0])         #Zeroth index is the headers
bits[0]
# weight  group

#print(bits[1])           #oneth index is the first data point, made up of 2 elemens, each correspoding to weight and group columns
bits[1]
# 4.17    ctrl

bits[1].split("\t")
# print(bits[1].split("\t"))      #To split the data element on tab and get each column separately
# ['4.17', 'ctrl']                #Both elements in the list are in quotes, indicating that the split element contained numbers
                                  #but even those in string format
#Basically the data is not automatically converted to its appropriate type.
#Python leaves it upto me to convert it to string or list or integer later on 
#for my specific purpose and task


# repr gives a literal representation of the data than just print. 
repr(contents)
# print(repr(contents))
# 'weight\tgroup\n4.17\tctrl\n5.58\tctrl\n5.18\tctrl\n6.11\tctrl\n4.5\tctrl\n4.61\tctrl\n5.17\tctrl\n4.53\tctrl\n5.33\tctrl\n5.14\tctrl\n4.81\ttrt1\n4.17\ttrt1\n4.41\ttrt1\n3.59\ttrt1\n5.87\ttrt1\n3.83\ttrt1\n6.03\ttrt1\n4.89\ttrt1\n4.32\ttrt1\n4.69\ttrt1\n6.31\ttrt2\n5.12\ttrt2\n5.54\ttrt2\n5.5\ttrt2\n5.37\ttrt2\n5.29\ttrt2\n4.92\ttrt2\n6.15\ttrt2\n5.8\ttrt2\n5.26\ttrt2\n'
contents
# print(contents)
# weight  group
# 4.17    ctrl
# 5.58    ctrl
# 5.18    ctrl
# 6.11    ctrl
# 4.5     ctrl
# 4.61    ctrl
# 5.17    ctrl
# 4.53    ctrl
# 5.33    ctrl
# 5.14    ctrl
# 4.81    trt1
# 4.17    trt1
# 4.41    trt1
# 3.59    trt1
# 5.87    trt1
# 3.83    trt1
# 6.03    trt1
# 4.89    trt1
# 4.32    trt1
# 4.69    trt1
# 6.31    trt2
# 5.12    trt2
# 5.54    trt2
# 5.5     trt2
# 5.37    trt2
# 5.29    trt2
# 4.92    trt2
# 6.15    trt2
# 5.8     trt2
# 5.26    trt2


for line in bits[0:5]:
    pass
    # print(line)
# weight  group
# 4.17    ctrl
# 5.58    ctrl
# 5.18    ctrl
# 6.11    ctrl

bits[0:5].pop()
# print(bits[0:5].pop())
for line in bits[0:5].pop():
    pass
    # print(line)
# 6.11    ctrl
# 6
# .
# 1
# 1

# c
# t
# r
# l


bits[-5:]
# print(bits[-5:]) #Last 5 elements of the bits list
# ['4.92\ttrt2', '6.15\ttrt2', '5.8\ttrt2', '5.26\ttrt2', '']     
# #There is an empty string '' at the end of this list along with the data elements. 
# It is called a trailing whitespace. That is due to the .read() method used on contents.
#We can eliminate that using .readlines() method. 


my_file = open("plantgrowth.txt")
contents = my_file.read()
repr(contents)
# print(repr(contents))
# 'weight\tgroup\n4.17\tctrl\n5.58\tctrl\n5.18\tctrl\n6.11\tctrl\n4.5\tctrl\n4.61\tctrl\n5.17\tctrl\n4.53\tctrl\n5.33\tctrl\n5.14\tctrl\n4.81\ttrt1\n4.17\ttrt1\n4.41\ttrt1\n3.59\ttrt1\n5.87\ttrt1\n3.83\ttrt1\n6.03\ttrt1\n4.89\ttrt1\n4.32\ttrt1\n4.69\ttrt1\n6.31\ttrt2\n5.12\t
# trt2\n5.54\ttrt2\n5.5\ttrt2\n5.37\ttrt2\n5.29\ttrt2\n4.92\ttrt2\n6.15\ttrt2\n5.8\ttrt2\n5.26\ttrt2\n'
#As we can see the .read() method led to a trailing \n newline character at the end of the string, which is in line with the fact
# that every data element in a row ends with a newline.


my_file = open("plantgrowth.txt")
contents = my_file.readlines()
repr(contents)
# print(repr(contents))
# ['weight\tgroup\n', '4.17\tctrl\n', '5.58\tctrl\n', '5.18\tctrl\n', '6.11\tctrl\n', '4.5\tctrl\n', '4.61\tctrl\n', '5.17\tctrl\n', '4.53\tctrl\n', '5.33\tctrl\n', '5.14\tctrl\n', '4.81\ttrt1\n', '4.17\ttrt1\n', '4.41\ttrt1\n', '3.59\ttrt1\n', '5.87\ttrt1\n', '3.83\ttrt1\n', '6.03\ttrt1\n', '4.89\ttrt1\n', '4.32\ttrt1\n', '4.69\ttrt1\n', '6.31\ttrt2\n', '5.12\ttrt2\n', '5.54\ttrt2\n', '5.5\ttrt2\n', '5.37\ttrt2\n', 
# '5.29\ttrt2\n', '4.92\ttrt2\n', '6.15\ttrt2\n', '5.8\ttrt2\n', '5.26\ttrt2\n']

first_line = contents[0]
repr(first_line)
first_line
# print(repr(first_line))
# print(first_line)
# 'weight\tgroup\n'
# weight  group


my_file = open("plantgrowth.txt")
for x in my_file:
    pass
    # print(repr(x))

my_file.close()
my_file.close()


################################################################################
#!/usr/bin/env python
import sys
sys.argv        # gives us any number of command line arguments in a list form i.e. the 
                # name of the script we are running followed by any and all arguments we type
# print(sys.argv) 
# (python_ds_handbook) rajan@Rajan:BIOL7200$ ./1_reading_and_data_exploration.py       
# ['./1_reading_and_data_exploration.py']
# (python_ds_handbook) rajan@Rajan:BIOL7200$ ./1_reading_and_data_exploration.py 1   2  type
# ['./1_reading_and_data_exploration.py', '1', '2', 'type']
# (python_ds_handbook) rajan@Rajan:BIOL7200$ ./1_reading_and_data_exploration.py 1_reading_and_data_exploration.py plantgrowth.txt 123 ine two three
# ['./1_reading_and_data_exploration.py', '1_reading_and_data_exploration.py', 'plantgrowth.txt', '123', 'ine', 'two', 'three']

type(sys.argv)
# print(type(sys.argv))
# <class 'list'>


file = open(sys.argv[0])
print(file.read())