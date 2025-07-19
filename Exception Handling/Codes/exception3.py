# In Python, write an interactive calculator. Take input as command line arguments, which is assumed to be a formula that consist of a number, an operator (at least + and -), and another number, separated by white space (e.g. 1 + 1). Check whether the input arguments are valid before computing the result:

# If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.

# Try to convert the first and third input to a float (like so: float_value = float(str_value)). Catch any ValueError that occurs, and instead raise a FormulaError

# If the second input is not '+' or '-', again raise a FormulaError

# If the input is valid, perform the calculation and print the result, else  print appropriate error messages and quit.

class FormulaError(Exception): pass

def length_check(lst) :
	try :
		if len(lst)!=3 :
			raise FormulaError("Invalid number of elements")
			return FormulaError
	except :
		print("Invalid number of elements")
		return FormulaError("Invalid number of elements")

def evalute(lst) :
	try :
		a = float(lst[0])
		b = float(lst[2])
	except :
		print("Invalid operands")
		return FormulaError("Invalid operands")
	try :
		if lst[1] == '+':
			val = a+b
			return val
		elif lst[1] == '-' :
			val = a-b
			return val
		else :
			print("Invalid operator")
			return FormulaError("Invalid operator")
	except :
		print("Invalid operator")
		return FormulaError("Invalid operator")

while True:
	exp = input("Enter the expression(type quit to terminate) : ")
	if exp=="quit" :
		exit(1)
	lst = exp.split()
	if length_check(lst) != FormulaError :
		val = evalute(lst)
		print(val)
			


















