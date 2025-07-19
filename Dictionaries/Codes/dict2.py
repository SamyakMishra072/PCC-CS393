#  Write a python Program to create grade calculator, creating a dictionary which consists of the student name, assignment result test results and their respective lab results.

# Given different scored marks of students. We need to find grades. The test score is an average of the respective marks scored in assignments, tests and lab-works. The final test score is assigned using below formula.

# 10 % of marks scored from submission of Assignments

# 70 % of marks scored from Test

# 20 % of marks scored in Lab-Works

#                 Grade will be calculated according to :

# score >= 90 : "A"

# score >= 80 : "B"

# score >= 70 : "C"

# score >= 60 : "D"

 

# Example input:

# james = { "name":"James Potter",

#           "assignment" : [82, 56, 44, 30],

#           "test" : [80, 80],

#           "lab" : [67.90, 78.72]

#         }

# Example output:

# Average marks of James Potter is : 75.962

# Letter Grade of James Potter is : C

d={}
res={}
d["name"]=input('Enter your name : ')
d["assignment"]=list(map(float, input('Enter the assignment marks : ').split()))
d["test"]=list(map(float, input('Enter the test marks : ').split()))
d["lab"]=list(map(float, input('Enter the lab marks : ').split()))

avg = 0.1*(sum(d["assignment"])/len(d["assignment"]))+0.7*(sum(d["test"])/len(d["test"]))+0.2*(sum(d["lab"])/len(d["lab"]))

if avg>=90:
	ch="A"
elif avg>=80:
	ch="B"
elif avg>=70:
	ch="C"
elif avg>=60:
	ch="D"
else:
	ch='Fail'
	
print('Average marks of',d["name"],'is',avg)
print('Letter Grade of',d["name"],'is',ch)


