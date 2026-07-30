#!/usr/bin/env python

import sys
sys.argv        # gives us any number of command line arguments in a list form i.e. the 
                # name of the script we are running followed by any and all arguments we type
# print(sys.argv) 
# (python_ds_handbook) rajan@Rajan:BIOL7200$ ./2_command_line_arguments.py       
# ['./2_command_line_arguments.py']
# (python_ds_handbook) rajan@Rajan:BIOL7200$ ./2_command_line_arguments.py  1 2            type djabka
# ['./2_command_line_arguments.py', '1', '2', 'type', 'djabka']
# (python_ds_handbook) rajan@Rajan:BIOL7200$ ./2_command_line_arguments.py 1_reading_and_data_exploration.py plantgrowth.txt 123 ine two three
# ['./2_command_line_arguments.py', '1_reading_and_data_exploration.py', 'plantgrowth.txt', '123', 'ine', 'two', 'three']

type(sys.argv)
# print(type(sys.argv))
# <class 'list'>
#Since sys.argv is a list, we can do all list operatinos on it.

sys.argv[1]
# print(sys.argv[1])
# (python_ds_handbook) rajan@Rajan:BIOL7200$ ./2_command_line_arguments.py  123 alpha beta gamm     spiderman
# 123                  # 123 was the oneth indexed element among all the arguments typed in command line

sys.argv[3]
# print(sys.argv[3])
# (python_ds_handbook) rajan@Rajan:BIOL7200$ ./2_command_line_arguments.py a b c delta
# c                    # c was the 3rd indexed element among all the arguments typed in command line

#For eg. we can index the zeroth element of the list
file = open(sys.argv[0])
file.read()
# print(file.read())
file.close()

#This types out our entire script in the terminal coz the first argument is the name of our script 
# (python_ds_handbook) rajan@Rajan:BIOL7200$ ./2_command_line_arguments.py a b c delta
"""
#!/usr/bin/env python

import sys
sys.argv        # gives us any number of command line arguments in a list form i.e. the 
                # name of the script we are running followed by any and all arguments we type
# print(sys.argv) 
# (python_ds_handbook) rajan@Rajan:BIOL7200$ ./2_command_line_arguments.py       
# ['./2_command_line_arguments.py']
# (python_ds_handbook) rajan@Rajan:BIOL7200$ ./2_command_line_arguments.py  1 2            type djabka
# ['./2_command_line_arguments.py', '1', '2', 'type', 'djabka']
# (python_ds_handbook) rajan@Rajan:BIOL7200$ ./2_command_line_arguments.py 1_reading_and_data_exploration.py plantgrowth.txt 123 ine two three
# ['./2_command_line_arguments.py', '1_reading_and_data_exploration.py', 'plantgrowth.txt', '123', 'ine', 'two', 'three']

type(sys.argv)
# print(type(sys.argv))
# <class 'list'>
#Since sys.argv is a list, we can do all list operatinos on it.

sys.argv[1]
# print(sys.argv[1])
# (python_ds_handbook) rajan@Rajan:BIOL7200$ ./2_command_line_arguments.py  123 alpha beta gamm     spiderman
# 123                  # 123 was the oneth indexed element among all the arguments typed in command line

sys.argv[3]
# print(sys.argv[3])
# (python_ds_handbook) rajan@Rajan:BIOL7200$ ./2_command_line_arguments.py a b c delta
# c                    # c was the 3rd indexed element among all the arguments typed in command line

#For eg. we can index the zeroth element of the list
file = open(sys.argv[0])
print(file.read())
#This types out our entire script in the terminal coz the first argument is 
#the name of our script 
"""


file = open(sys.argv[1])
file.read()
# print(file.read())

#This types out all the content in the file plantgrowth.txt coz that file name
#is the argument indexed one as shown below:
# rajan@Rajan:BIOL7200$ ./2_command_line_arguments.py plantgrowth.txt a b c 
"""
weight  group
4.17    ctrl
5.58    ctrl
5.18    ctrl
6.11    ctrl
4.5     ctrl
4.61    ctrl
5.17    ctrl
4.53    ctrl
5.33    ctrl
5.14    ctrl
4.81    trt1
4.17    trt1
4.41    trt1
3.59    trt1
5.87    trt1
3.83    trt1
6.03    trt1
4.89    trt1
4.32    trt1
4.69    trt1
6.31    trt2
5.12    trt2
5.54    trt2
5.5     trt2
5.37    trt2
5.29    trt2
4.92    trt2
6.15    trt2
5.8     trt2
5.26    trt2
"""

file.close()