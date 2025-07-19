# Write a Python program to generate a random alphabetical string, random value between two integers (inclusive) and a random multiple of 7 between 0 and 70.

# NOTE: Generate a random alphabetical string:

# lGhPpBDqfCgXKzSbGcnmcDWBEZeiqcUqztgvwcXfVyPslOggKdbIxOejJfFMgspqrgskanNYpscJEOVIpYkGGNxQlaqeeubGDbQSBhBedrdOyqOmKPTZvzKmKVoids

# Generate a random value between two integers, inclusive:

# 0

# 4

# 1

# Generate a random multiple of 7 between 0 and 70:

# 70

import random
max = int(input("Enter max length : "))
lst = list(range(65,91)) + list(range(97,123))
s = ""
i = random.randint(1,max)
for j in range(i) :
    ch = chr(random.choice(lst))
    s += ch
print("The string is :",s)

l = int(input("Enter the lower limit : "))
u = int(input("Enter the upper limit : "))
val = random.randint(l,u)
print("A random value between",l,"and",u,"is :",val)

val1 = random.randint(1,10) * 7
print("A random multiple of 7 is :",val1)
