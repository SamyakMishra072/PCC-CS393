# Write a Python function to multiply all the numbers in a list.

#      Sample List: [8, 2, 3, -1, 7]

#      Expected Output: -336

def multiply(my_list):
	p=1
	for i in my_list:
		p=p*i
	print('The required product is : ',p)


my_list = list(map(int, input('Enter numbers in the list : ').split()))
multiply(my_list)
