# Write a python program to Add Tuple to List and vice – versa.

mylist=list(map(int, input('Enter the elements in the list(separated by spaces) : ').split()))
mytuple=tuple(map(int, input('Enter the elements in the tuple(separated by spaces) : ').split()))
print('The list input by the user is:',mylist)
print('The tuple input by the user is:',mytuple)


mylist.append(mytuple)

mytuple=list(mytuple)
mytuple.append(mylist[:-1])
mytuple=tuple(mytuple)


print('The new list after adding tuple is :',mylist)
print('The new tuple after adding list is:',mytuple)
