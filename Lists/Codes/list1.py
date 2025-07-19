#Write a program in Python to interchange the first and last elements in a list.

l=[]
s=int(input('Enter the size of the list : '))
for i in range(0,s,1):
    a=int(input('Enter a number : '))
    l.append(a)
print('The original list is : ')
print(l)
temp=l[0]
l[0]=l[s-1]
l[s-1]=temp

print('The resulting list is : ')
print(l)
    
        	
