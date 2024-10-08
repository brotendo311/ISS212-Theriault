# Author: Andy Theriault
# Week 4 Assignment 3 # Scenario 3: Data Security Tax Calculation
# Code adapted from walkthrough

#Get data usage from user.
data_usage=float(input("Enter your annual data usage in MB: "))

#calculate data tax!
if data_usage<=85528:
    tax=data_usage*.18
else:
    #calculate tax for overage!
    tax=14839.02+(0.32*(data_usage-85528))
tax=max(tax,0)
print(f'Your Data Security Tax is : {round(tax)} MB')
