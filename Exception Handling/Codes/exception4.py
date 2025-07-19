# Imagine you have a file named data.txt. Open it for reading using Python code, but make sure to use a try block to catch an exception that arises if the file doesn't exist. Once you've verified your solution works with an actual file, delete the file and see if your try block is able to handle it.

# Note that the exception we need to watch out for is FileNotFoundError.

try :
	with open("data.txt","r") as file :
		content = file.read()
		print("Content of the file, 'data.txt' : ")
		print(content)
except Exception as e :
	print("ERROR :",e)
