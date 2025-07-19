# Write a Python program to write a list to a file.

lst = list(map(int,input("Enter the elements of the list : ").split()))
name = input("Enter the name of the file : ")
try :
	with open(name,"w") as file :
		file.write(str(lst))
		
except Exception as e :
	print("ERROR :",e)
