# Write a Python function to find the Max of three numbers.

def maximum(a,b,c):
	if a>b and a>c:
		return a
	elif b>a and b>c:
		return b
	else:
		return c
		
a=int(input('Enter the first number : '))
b=int(input('Enter the second number : '))
c=int(input('Enter the third number : '))

result = maximum(a,b,c)

print('The maximum of the three numbers is :',result)

