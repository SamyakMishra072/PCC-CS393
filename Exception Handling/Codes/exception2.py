# The code below assigns the 5th letter of each word in 'food' to the new list fifth. However, the code currently produces errors. Insert a try/except clause that will allow the code to run and produce a list of the 5th letter in each word. If the word is not long enough, it should not print anything out. Note: The 'pass' statement is a null operation; nothing will happen when it executes.

# food = ["chocolate", "chicken", "corn", "sandwich", "soup", "potatoes", "beef", "lox", "lemonade"]

# fifth = []

# for x in food:

#     fifth.append(x[4])

food = ["chocolate", "chicken", "corn", "sandwich", "soup", "potatoes", "beef", "lox", "lemonade"]

fifth = []

for x in food:
    try :
        fifth.append(x[4])
    except :
        pass
print(fifth)