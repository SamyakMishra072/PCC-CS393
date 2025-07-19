#Write a program that keeps on accepting numbers from the user until the user enters Zero. Display the sum and average of all the numbers.

sum = 0
count = 0
while 1:
   n = int(input("Enter a number : "))
   if n==0:
   	break
   else:
   	sum = sum+n
   	count = count + 1
   	
if count!=0:
	print("The sum is : ",sum)
	print("The average is : ",sum/count)
else:
   print("Zero entered!!")
