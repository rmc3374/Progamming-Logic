def printthepage(obj): 
    pring(obj)

GRATUITY_RATE = .16


# if going to write redundant code, etc. use function
# functions written above code because it is loaded into computer memory ready to be pulled out and used
def checkInput(input): 
    if (not input.isnumeric()): 
        return f'{input} is not numeric. Please try again.'
    
    elif (int(input) > 10 or int(input) < 1): 
        return f'{input} is out of bounds. Please try again.'

    # Happy path
    return f'The number is {input}'

# Iterative Statements

# Decision Structures
response = input("Please enter a number between 1 and 10: ")
print(checkInput(response))

# there are functions in Python that check for unwanted digits, symbols, etc.
#   most languages require user to write function, Python has prewritten function
#   isdigit checks to see if all values are digits; isnumeric checks if values can be converted into numbers

# if (not response.isnumeric()): 
    # print(f'{response} is not numeric. Please try again.')
# elif (int(response) > 10 or int(response) < 1): 
    # print(f'{response} is out of bounds. Please try again.')
# else: 

# 1 "=" is assigning value to something, "==" is assigning equality to something
    # Java has "===" which checks if both sides are equal, along with the types of values being the same (i.e. float, string, etc.)
# (response == 445)

    # print(f'The number is {response}')

# Can do string concatination instead of previous print statement - professor prefers previous statement for readability
    # print('The number is ' + response)

# Selection Statements / Structure
# strings are imutable, not mutable
    # firstnameofthedog = '45'
    # lastname = '45'
    # age = 45 + 45.0
    # printthepage(age)