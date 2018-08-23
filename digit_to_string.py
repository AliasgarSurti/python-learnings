'''
This program's intention is to convert the digit passed in the argument to the string.
Each digit is stored in array and then it is printed at last.
e.g. python3.6 digit_to_string.py 56
output:['five','six']

Author: Aliasgar Surti
Date: 23 August 2013
'''
import sys

numberInStrings = ['zero','one','two','three','four','five','six','seven','eight','nine']

def numberToString(number):
	try:
		return numberInStrings[int(number)]
	except ValueError as err:
		print (err)
		exit()

try:
	digit = sys.argv[1]
	listOfDigits = []
	lengthOfDigit = len(digit)
	param = 0
	digitInInt = int(digit) # Only to check whether an int is passed.
	while lengthOfDigit:
		#print (numberToString(digit[param])) # To print digit individually
		list.append(listOfDigits,numberToString(digit[param])) # To print digits in array (list)
		param += 1
		lengthOfDigit -= 1
	print (listOfDigits)

except ValueError as err:
	print (err)
	exit()

except IndexError as err:
	print ("usage: python3.6 digit_to_string.py 56")
	print (err)
	exit()
