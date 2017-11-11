# Line 7: defines a function named some_basic_math and takes two arguments a & b.
# Line 8: adds the two variables together.
# Line 10: passes 3 & 4 as the arguments and prints the answer, 7.
# Line 11: passes hello & world and prints the two strings together (with no space).
# Line 12: trys to concatenate an integer and a string, which throws an TypeError Exception

def some_basic_math(a, b):
	print a + b
	
some_basic_math(3, 4)
some_basic_math("hello", "world")
some_basic_math(5, "hello")
