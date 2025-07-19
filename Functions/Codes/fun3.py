#  Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. 

#      Sample Input: 'The quick Brown Fox'

#      Expected Output:

#      No. of Upper case characters: 3

#      No. of Lower case Characters: 13

def check(a):
	lower=upper=0
	for i in a:
		if i.islower():
			lower=lower+1
		elif i.isupper():
			upper=upper+1
	print('No. of Upper case characters:',upper)
	print('No. of Lower case characters:',lower)
			
a=input('Enter the string : ')
check(a)
