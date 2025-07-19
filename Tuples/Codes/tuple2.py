#Write a python program to Copy specific elements from one tuple to a new tuple

tuple1=()
index=[]
tuple2=()
l1=list(tuple1)
l2=list(tuple2)

s1=int(input('Enter the size of the first tuple : '))
for i in range(s1):
	a=int(input('Enter a number : '))
	l1.append(a)
tuple1=tuple(l1)

j=input('Enter the indices with spaces : ')
index=j.split(' ')


for i in range(len(index)):
     l2.append(l1[int(index[i])])
     
tuple2=tuple(l2)

print('The original tuple is : ',tuple1)
print('The tuple formed after copying specific elements is : ',tuple2)



	



