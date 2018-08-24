'''
This program's intention is to convert the digit passed in the argument to the string.
Each digit is stored in array and then it is printed at last.
e.g. python3.6 digit_to_string.py 56
output:['five','six']

Author: Aliasgar Surti
Date: 24 August 2013
'''
import sys
import bigDigits as digits

numberInStrings = [digits.Zero, digits.One, digits.Two,\
					digits.Three, digits.Four, digits.Five,\
					digits.Six, digits.Seven, digits.Eight,\
					digits.Nine]

def numberToString(number):
	try:
		return numberInStrings[int(number)]
	except ValueError as err:
		print (err)
		exit()

try:
	digit = sys.argv[1]
	listOfDigits = []
	param = 0
	digitInInt = int(digit) # Only to check whether an int is passed.
	numberOfElements = 7
	unit = 0
	while param < numberOfElements:
		line = ""
		lengthOfDigit = len(digit)
		while lengthOfDigit:
			line += numberToString(digit[unit])[param]
			line += "   "
			lengthOfDigit -= 1
		print (line)
		param += 1
		#unit += 1

except ValueError as err:
	print (err)
	exit()

except IndexError as err:
	print ("usage: python3.6 digit_to_string.py 56")
	print (err)
	exit()
