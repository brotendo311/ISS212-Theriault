# Author : Andy Theriault
# Code adapted from walkthrough


# I commented out my function that I used to establish which years would work for the assignment
#def pcycle(year):

#gather input from user.
year = int(input("Enter the year to check the patch cycle: "))
if year < 2000:
	print("Not within the managed patch period.")
else:
	if year % 4 != 0:
		print("Standard Year")
	elif year % 100 != 0:
		print("Patch Year")
	elif year % 400 != 0:
		print("Standard Year")
	else:
		print("Patch Year")

#for i in range(2000,2100):
	#print(f'The year {i} is...')
	#pcycle(i)

