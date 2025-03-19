# input variables
# employee name
employeeName = input("Please enter employee name: ")

# number of shifts
shifts = int(input("Please enter number of shifts: "))

# number of transactions
transactionAmount = int(input("Please enter the number of transactions: "))

# transaction dollar value
transactionValue = float(input("Please enter the transaction dollar value: "))

# calculate productivity score
# productivity score = (employee transaction dollar value / number of transactions) / number of shifts worked

productivityScore = (transactionValue/transactionAmount) / shifts

# calculate bonus
if productivityScore <= 30: 
    employeeBonus = 50.00
elif 31 <= productivityScore <= 69: 
    employeeBonus = 75.00
elif 70 <= productivityScore <= 199: 
    employeeBonus = 100.00
elif productivityScore >= 200: 
    employeeBonus = 200.00

# print employeeName
print(f"Employee Name: {employeeName}")
print(f"Employee Bonus: $ {employeeBonus}")