# Write a Python program to calculate surface volume and area of a cylinder. Go to the editor

# Note: A cylinder is one of the most basic curvilinear geometric shapes, the surface formed by the points at a fixed distance from a given straight line, the axis of the cylinder.

# Test Data:

# volume: Height (4), Radius (6)

# Expected Output:

# Volume is: 452.57142857142856

# Surface Area is: 377.1428571428571

import math

r=float(input("Enter the radius of the cylinder : "))
h=float(input("Enter the height of the cylinder : "))

v=math.pi*r*r*h

choice=int(input('Enter 1 for open cylinder\nEnter 2 for closed cylinder: '))

if choice==1:
	s=2*math.pi*r*h
else:
	s=2*math.pi*r*h + 2*math.pi*r*r
	
print("Volume is: ",v)
print("Surface Area is: ",s)

