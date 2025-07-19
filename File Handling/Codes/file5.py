#Write a Python program to take a file name and a string pattern from the user. Now print the number of occurrence of the pattern string found in the file.

name = input("Enter the name of the file : ")
s = input("Enter the string : ")
count = 0
try :
	with open(name,"r") as file :
		lst = (file.read()).split("\n")
		for i in lst :
			words = i.split()
			for j in words : 
				if j == s : 
					count+=1
		print("Number of occurance of '{}' in '{}' is = {}".format(s,name,count))
		
except Exception as e :
	print("ERROR :",e)

