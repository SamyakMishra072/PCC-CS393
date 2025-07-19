# Write a program to print all prime numbers that fall between two numbers including both (accept two numbers from the user)

a = int(input("Enter the starting number : "))
b = int(input("Enter the ending number : "))
for i in range(a,b+1,1):
	flag = True
	if i==0 or i==1:
		flag = False
	else:
		for j in range(2,i,1):
			if i%j==0:
				flag = False
				break
	if flag==True:
		print(i)		
		
