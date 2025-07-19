#Write a program to find the factorial of a number.

num = int(input("Enter a number : "))
fact = 1
i = 1
if num==0:
	print("The factorial of",num,"is : ",fact)
else:
	while i<=num:
		fact = fact * i
		i = i+1
	print("The factorial of",num,"is : ",fact)
