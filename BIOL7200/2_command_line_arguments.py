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


file = open(sys.argv[0])
print(file.read())
#This types out our entire script in the terminal coz the first argument is 
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


file = open(sys.argv[0])
print(file.read())

"""