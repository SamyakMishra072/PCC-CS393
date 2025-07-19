#Write a Python program to sort a string lexicographically.

string = input("Enter the string : ")
l=(sorted(string))
s=''
for i in l:
  s=s+i
print('The lexicographically sorted string is : ',s)

