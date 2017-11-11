# Line 5: defines a function called 'print_hello_world', that takes an argument of (x)
# Line 6: defines what the function will do (print a string & a new line) the number of time defined by "x"
# Line 8: calls the function with an argument of 3, which is passed as the variable "x"

def print_hello_world(x):
	print "Hello World!\n" * x
	
print_hello_world(3)
