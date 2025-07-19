#Write a Python program to copy the contents of a file to another file .

s = input("Enter the name of the source file : ")
t = input("Enter the name of the target file : ")
try :
	with open(s,"r") as file :
		lst = (file.read()).split("\n")
	with open(t,"w") as f :
		st = "\n".join(lst)
		f.write(st)
		
except Exception as e :
	print("ERROR :",e)
