def checkInput(input): 
    # Decision Structures
    if (not input.isnumeric()): 
        return f'{input} is not numeric. Please try again.'
    
    if (int(response) > 10 or int(response) < 1): 
        return f'{input} is out of bounds. Please try again.'
    # happy path
    return f'The number is {input}'

# Iterative Statements
# response = input("Please enter a number between 1 and 10: ")

# Do not put Boolean expressions here inside While loop - Line 15
# while (response != -1): 

# Best practice for looping in Python
while (True): 
    response = input("Please enter a number between 1 and 10: ")
    print(checkInput(response))