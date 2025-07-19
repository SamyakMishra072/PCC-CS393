# Write a Python program to read first n lines of a file

name = input("Enter the name of the file : ")
try :
	with open(name,"r") as file :
		n = int(input("Enter the number of lines to be printed : "))
		lst = (file.read()).split("\n")
		if n>len(lst) :
			print("{} has only {} lines .".format(name,len(lst)))
			print("Displaying first {} lines from file, {} : ".format(len(lst),name))
			for i in range(n) :
				print(lst[i])
		else :
			print("Displaying first {} lines from file, {} : ".format(n,name))
			for i in range(n) :
				print(lst[i])
		
except Exception as e :
	print("ERROR :",e)
