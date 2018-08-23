'''
The sole purpose of this program is to demonstrate the argument passing via command line.
If the program is called as "python3.6 passing_arguments.py hello" the sys.argv will
contain ['passing_arguments.py', 'hello'].
The output of this script are the parameters passed to the script.

Author: Aliasgar Surti
Date: 23 August 2018
'''

import sys

if len(sys.argv) == 1:
	print ("Call this script by some arguments")
	exit()

length = len(sys.argv)
param = 1
length -= param

while length:
	print ("Parameter " + str(param) + " is " + sys.argv[param])
	param += 1
	length -= 1
