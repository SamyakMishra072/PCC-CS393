# Write a Python program to count the number of lines in a text file. 

name = input("Enter the name of the file : ")
try :
	with open(name,"r") as file :
		lst = (file.read()).split("\n")
		n = len(lst)
		n-=1
		print("Number of lines in",name,"is =",n )
		
except Exception as e :
	print("ERROR :",e)
