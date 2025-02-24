# input statements
salary = float(input("Please enter salary: "))
numDependents = float(input("Please enter number of dependents: "))

# calculate taxes here
stateTaxPercentage = 0.065
federalTaxPercentage = 0.28
dependentDeduction = 0.025

stateTax = salary * stateTaxPercentage
federalTax = salary * federalTaxPercentage
dependents = (dependentDeduction * salary) * numDependents

totalWithholding = stateTax + federalTax + dependents
takeHomePay = salary - totalWithholding

# output statements
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
