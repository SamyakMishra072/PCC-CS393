#Input two tuples and write a python program to find Modulo of tuple elements and store in a third tuple.

tuple1 = tuple(map(int, input('Enter elements in the first tuple(separated by spaces): ').split()))
tuple2 = tuple(map(int, input('Enter elements in the first tuple(separated by spaces and of the same size as the first tuple): ').split()))
l = []
for i in range(len(tuple1)):
	l.append(tuple1[i]%tuple2[i])
l=tuple(l)

print('The first tuple is : ',tuple1)
print('The second tuple is : ',tuple2)
print('The resultant tuple is : ',l)


