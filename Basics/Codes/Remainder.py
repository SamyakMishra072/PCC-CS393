# Write a python program to find remainder when a number is divided by z.

num = int(input("Enter the number to be divided : "))
div = int(input("Enter the divisor : "))
if div == 0:
	print("Invalid divisor, zero division error!!")
else:
	print("The remainder when",num,"is divided by",div,"is",num%div)

