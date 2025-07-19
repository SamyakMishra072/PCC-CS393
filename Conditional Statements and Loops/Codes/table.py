#Write a program to print a table of a number accepted from the user.

num = int(input("Enter a number : "))
i = 1
print("The table of",num,"(upto 10) is : ")
while i<=10:
	print(num,"X",i,"=",num*i)
	i=i+1
	
