#Write a python program to Reverse a List.

l=[]
s=int(input('Enter the size of the list : '))
for i in range(0,s,1):
    a=int(input('Enter a number : '))
    l.append(a)
print('The original list is : ')
print(l)
l.reverse()
print('The reversed list is : ')
print(l)

