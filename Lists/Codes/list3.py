#Write a Python program to count Even and Odd numbers in a List.

l=[]
counteven=0
countodd=0
s=int(input('Enter the size of the list : '))
for i in range(0,s,1):
    a=int(input('Enter a number : '))
    l.append(a)
print('The original list is : ')
print(l)

for i in range(0,s,1):
    if l[i]%2==0:
       counteven=counteven+1
    else:
       countodd=countodd+1

print('The number of even numbers in the list is :',counteven)
print('The number of odd numbers in the list is :',countodd)
