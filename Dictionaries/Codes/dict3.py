# Write a program to create two Dictionaries. Take a key from the 1st dictionary and find it in the 2nd dictionary. Display the corresponding value if found otherwise print appropriate message.

# Also merge the two dictionaries and display the output.

dict1={}
dict2={}
flag=0
s1=int(input('Enter the size of the dictionary 1: '))

for i in range(s1):
	key = input('Enter the key : ')
	val = input('Enter the corresponding value : ')
	dict1[key] = val
	
s2=int(input('Enter the size of the dictionary 2: '))

for i in range(s2):
	key = input('Enter the key : ')
	val = input('Enter the corresponding value : ')
	dict2[key] = val
	
for i in dict1:
	if i in dict2:
		print(i,':',dict1[i])
		flag=1
if flag==0:
    print("Key not found")
		
newdict = {**dict1 , **dict2}
print(newdict)


