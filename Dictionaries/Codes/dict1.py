# Write a python program to create a dictionary and do the following:

#      a)       Sort Dictionary by key.

#      b)      Sort Dictionary by value.

d = {}
res = {}
temp={}
res2={}
n=int(input('Enter the number of values for input : '))

for i in range(n):
	key = input('Enter the key : ')
	val = input('Enter the corresponding value : ')
	d[key] = val

keylist= list(d.keys())

val_list=list(d.values())	
for i in range(len(d)):
	temp[val_list[i]]=keylist[i]
val_list.sort()
res2={temp[j]:j for j in val_list}

keylist.sort()

for i in range(len(keylist)):
	res[keylist[i]]=d[keylist[i]]
print('The dictionary sorted by key is : ',res)

	
print('The dictionary sorted by value is : ',res2)


