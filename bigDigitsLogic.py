'''
This program's intention is to convert the digit passed in the argument to the string.
Each digit is stored in array and then it is printed at last.
e.g. python3.6 digit_to_string.py 56
output:['five','six']

Author: Aliasgar Surti
Date: 24 August 2018
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
	while param < numberOfElements:
		unit = 0
		line = ""
		lengthOfDigit = len(digit)
		while lengthOfDigit:
			tempString = numberToString(digit[unit])[param]
			l = len(tempString)
			index = 0
			tempString1 = ""
			while l:
				if tempString[index] == "*":
					tempString1 += str(digit[unit])
				else:
					tempString1 += " "
				l -= 1
				index += 1
			line += tempString1
			unit += 1
			line += "   "
			lengthOfDigit -= 1
		print (line)
		param += 1
except ValueError as err:
	print (err)
	exit()
except IndexError as err:
	print ("usage: python3.6 digit_to_string.py 56")
	print (err)
	exit()
