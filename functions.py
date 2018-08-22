def accept_int(msg):
	try:
		a = int(input(msg))
		return a
	except ValueErr as err:
		print (err)

i = accept_int("enter an integer")
print ("you entered" + str(i))