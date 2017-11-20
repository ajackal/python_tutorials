def check_even_or_odd():
	x = raw_input("Input a number: ")

	try:
		if int(x) % 2 == 0:
			print "The number is even!"
		else:
			print "The number is odd!"
	except ValueError:
		print "Input must be an integer!"
	
check_even_or_odd()
