# Author : Andy Theriault
# Copied from Scenario 4

#def pcycle(year):
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

