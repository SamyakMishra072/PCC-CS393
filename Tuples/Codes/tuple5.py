#Write a Python program to create a list of tuples from given list having number and its cube in each tuple. (e.g. (2,8),(3,27),....).

l = list(map(int, input('Enter the numbers in the list(separated by spaces) : ').split()))
res=[]
print('The list input by the user is : ',l)

for i in l:
	t=(i,i**3)
	res.append(t)

print('The resultant list is : ',res)

