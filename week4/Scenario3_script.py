# Author: Andy Theriault
# Scenario 3: Data Security Tax Calculation

data_usage=float(input("Enter your annual data usage in MB: "))

if data_usage<=85528:
    tax=data_usage*.18
else:
    tax=14839.02+(0.32*(data_usage-85528))
tax=max(tax,0)
print(f'Your Data Security Tax is : {round(tax)} MB')
