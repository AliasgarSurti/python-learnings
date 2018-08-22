'''
The sole purpose of this program is to implement a wrapper to 'input' call which takes input from the user.
Also this code implements the exception handling by which user comes to know that they have entered integer other than integer.

Author: Aliasgar Surti
Date: 22 August 2018
'''
def accept_int(msg):
	try:
		a = int(input(msg))
		return a
	except ValueErr as err:
		print (err)

i = accept_int("enter an integer")
print ("you entered" + str(i))