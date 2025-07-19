# Write a python program to Replace words from Dictionary.

# e.g. Input : test_str = ‘TechnoIndia is one of the best colleges in India ’, repl_dict = {“India” : “West Bengal”}

# Output : TechnoIndia is one of the best colleges in West Bengal

# Explanation : “India” word is replaced by lookup value.

a = input("enter a string :")
l = a.split()
i =''
d = {"India":"West Bengal"}
l2=[]
for word in l:
	if word in d:
		l2.append(d[word])
	else:
		l2.append(word)
print(" ".join(l2))
