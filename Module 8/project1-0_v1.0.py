# import os to be able to open/use text file
import os

# load vehicles from file at start
def loadVehiclesFromFile(): 
    # if os.path.exists("C:\\Progamming Logic\\Module 8\\vehicleName.txt"):  
    with open("C:\\Progamming Logic\\Module 8\\vehicleName.txt", "r") as file: 
        authorizedVehicles = [line.strip() for line in file]
        return authorizedVehicles

# save vehicleName to file
def saveVehiclesToFile(vehicles): 
    with open("C:\\Progamming Logic\\Module 8\\vehicleName.txt", "w") as file: 
        for vehicle in vehicles: 
            file.write(vehicle + "\n")

#  onLoad - will pring display menu
def onLoad(): 
    while(True): 
        displayMenu()
        menuSelection = input(" ")
        # print authorizedVehicle list
        if (menuSelection == '1'): 
            print("The AutoCountry sales manager has authorized" \
            " the purchase and selling of the following vehicles: ")
            listAuthorizedVehicles()
        # enter full vehicle name and print if authorized or not
        if (menuSelection == '2'): 
            checkVehicleName()
        if (menuSelection == '3'): 
            addVehicleName()
        # end menu selection and close
        if (menuSelection == '4'): 
            deleteVehicleName()
        if (menuSelection == '5'): 
            print("Thank you for using the AutoCountry" \
                   " Vehicle Finder, good-bye!")
            break

    
# displayMenu shows:
def displayMenu(): 
    print("****************")
    print("AutoCountry Vehicle Finder v0.5")
    print("****************")
    print("Please Enter the following number below " \
    " from the following menu: ")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit")

# create def for authorizedVehicles
def listAuthorizedVehicles(): 
    # print authorizedVehicles list
    for item in loadVehiclesFromFile():
            print(item)

# create def for vehicleName - need to print each name individually and state if its authorized or not
def checkVehicleName(): 
     # enter vehicle name
    vehicleName = input("Please Enter the full Vehicle name: ")
    if vehicleName in loadVehiclesFromFile():
        print(f"{vehicleName} is an authorized vehicle")
    else: 
        print(f"{vehicleName} is not an authorized vehicle, if you" \
               " received this in error please check the spelling"
               " and try again")
          
# create def for ADD vehicleName
def addVehicleName(): 
    vehicles = loadVehiclesFromFile()
    # global authorizedVehicles
    addName = input("Please Enter the full Vehicle" \
    " name you would like to add: ")
    # enter new vehicleName
    vehicles.append(addName)
    saveVehiclesToFile(vehicles)
    # print authorizedVehicles list with new vehicles added
    print(f'You have added "{addName}" as an authorized vehicle')

# create def for DELETE vehicleName
def deleteVehicleName(): 
    # enter vehicleName to remove
    deleteName = input("Please Enter the full Vehicle name you would" \
    " like to REMOVE: ")
    # print "Are you sure you want to remove "vehicleName" from the Authorized Vehicles List?"
    confirmName = input(f'Are you sure you want to remove ' \
                        f'"{deleteName}" from the Authorized Vehicles List?')
    # if true, do this
    if(confirmName == "yes"): 
        vehicles = loadVehiclesFromFile()
        if deleteName in vehicles: 
            vehicles = [vehicle for vehicle in vehicles if vehicle != deleteName]
            saveVehiclesToFile(vehicles)
            print(f'You have REMOVED "{deleteName}" as an authorized vehicle')


# final onLoad - prints what is shown in onLoad def function
onLoad()

