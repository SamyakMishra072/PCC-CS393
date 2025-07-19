# Use comparison operator to find out whether a given variable ‘a’ is greater than ‘b’ or not. For example, take a=34, b=80.

a = int(input("Enter the first value : "))
b = int(input("Enter the second value : "))
if a > b :
	print(a, "is greater than", b)
elif b > a :
	print(b, "is greater than", a)
else :
	print("The two numbers are equal!!")
