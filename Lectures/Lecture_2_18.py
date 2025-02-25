# Taxes - 
# TAX_RATE
TAX_RATE = 0.13
RATE_OF_DEDUCTION = 2000

def calculate_tax(tax_rate):
        #  calculate tax bill (gross_income * TAX_RATE)
    tax_bill = gross_income * tax_rate

    # calculate rate of deduction
    dependent_deduction = RATE_OF_DEDUCTION * num_of_dependents

    # calculate tax subtotal
    tax_subtotal = tax_bill - dependent_deduction

    return tax_subtotal

# get dependents
num_of_dependents =float(input('Pls enter the number of dependents: '))

# get gross income
gross_income =float(input('Pls enter your gross income: '))

# get state
state_code = input('Pls enter your two digit state code: ')

if (state_code == 'CA'):
    # print tax subtotal
    print(f'Your final tax bill is ${calculate_tax(TAX_RATE)}')
elif (state_code == 'NY'):
    # print tax subtotal
    print('Your final tax bill is ${calculate_tax90.109)}')
else:
    print(f'Your final tax bill is ${calculate_tax(0.10)}')