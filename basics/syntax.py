# Assigning values to variables
x = 10 # int
pi = 3.14126539 # float
name = "Mac" # str
isReadyToMarry = True

# print the values and types
print(x, " is of type", type(x))
print(pi, " is of type", type(pi))
result = x * pi
print(result, " is of type", type(result))
result_string = str(result)
result_int = int(result)
print(result_int, "is of type ", type(result_int))
print(result_string, " is of type", type(result_string))
print(name, "'s variable is of type", type(name))
print(isReadyToMarry, " is of type: ", type(isReadyToMarry))


# Comments
# Things the python interpreter should avoid.
"""
Text here
More text here
Even more here.
"""

# Data types
# int, float, string
# booleans [bool]: True or False.

# Operators
"""
----- Arithmetic Operators
+  (addtion)
- (subtraction)
* (multiplication)
/ (division)
// (floor division)
% (modulus)
** (exponentiation)

---- Comparison operators
==, !=, >, <, >=, <=

---- Logical operators
and, or, not
"""

# Functions
# functions group related features together.
# they may/maynot return a value.
# they may/maynot accept 1 or more arguments/parameters.

# def accept_input():


is_even = (x % 2 == 0)
is_positive = (x > 0)

def check_x():
	print("====== start ======")
	print(is_even and is_positive) # True
	print(not is_even) # False

def close_door() -> bool:
	print("Door is closed now.")
	return True

def off_the_bulb():
	if close_door() == True:
		print("We have closed the door and turned off the bulb.")


def check_water_guage(guage: int):
	print(f"The guage is: {guage}")
	if guage > 200:
		print("The water is too full.")


if __name__ == "__main__":
	# off_the_bulb()
	# check_water_guage(150)
	check_x()

