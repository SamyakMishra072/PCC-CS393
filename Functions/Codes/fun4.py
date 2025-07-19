# Write a Python function that prints out the first n rows of Pascal's triangle.

#      Note: Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.
#      Each number is the two numbers above it added together.

def pascal(n):
	c=1
	for i in range(0,n):
		for k in range(1,n-i+1):
			print(' ',end=' ')
		for j in range(0,i+1):
			if j==0:
				c=1
			else:
				c=c*(i-j+1)//j;
			print(' ',c,end=' ')	
		print('\n')
	
n=int(input('Enter the number of rows : '))
pascal(n)
