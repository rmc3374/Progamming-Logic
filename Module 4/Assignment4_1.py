"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
# Charge for this sign.
charge = input("Please enter the cost of the sign: ")

# Number of characters.
numChars = input("Please enter the number of characters: ")

# Color of characters.
color = input("Please enter the color of the characters: ")

# Type of wood.
woodType = input("Please enter the type of wood: ")

# Write assignment and if statements here as appropriate.
def signCharge(numChars, color, woodType): 
    baseCharge = 35.00
    if numChars <= 5: 
        extraCharge = 0.00
    else: 
        extraChars = numChars - 5
        extraCharge = extraChars * 4
    if color() == "gold": 
        colorCharge = 15.00
    elif color() in ["black", "white"]: 
        colorCharge = 0.00
    if woodType() == "oak": 
        materialCharge = 20.00
    elif woodType() == "pine": 
        materialCharge = 0.00
charge = signCharge(numChars, color, woodType)   
# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))
