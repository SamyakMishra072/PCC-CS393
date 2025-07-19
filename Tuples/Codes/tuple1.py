#Write a python program to Swap two tuples in Python.

tuple1=()
tuple2=()
l1=list(tuple1)
l2=list(tuple2)

s1=int(input('Enter the size of the first tuple : '))
for i in range(s1):
	a=int(input('Enter a number : '))
	l1.append(a)
tuple1=tuple(l1)

s2=int(input('Enter the size of the second tuple : '))
for i in range(s2):
	a=int(input('Enter a number : '))
	l2.append(a)
tuple2=tuple(l2)

print('Initial condition is tuple1:',tuple1,'and tuple2:',tuple2)

tuple1, tuple2 = tuple2, tuple1

print('Swapped condition is tuple1:',tuple1,'and tuple2:',tuple2)

