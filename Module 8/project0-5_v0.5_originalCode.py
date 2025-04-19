# Deleted
#  global list of authorized vehicles
authorizedVehicles = ["Ford F-150", "Chevrolet Silverado",
                        "Tesla CyberTruck", "Toyota Tundra",
                          "Rivian R1T", "Ram 1500"]

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
                   "Vehicle Finder, good-bye!")
            break

    
# displayMenu shows:
def displayMenu(): 
    print("****************")
    print("AutoCountry Vehicle Finder v0.4")
    print("****************")
    print("Please Enter the following number below " \
    "from the following menu: ")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit")

# create def for authorizedVehicles
def listAuthorizedVehicles(): 
    # What are the authorized vehicles: Ford F-150, 
    #   Chevrolet Silverado, Tesla CyberTruck, Toyota Tundra, Nissan Titan
    # print authorizedVehicles list
    for item in authorizedVehicles:
            print(item)

# create def for vehicleName - need to print each name individually and state if its authorized or not
def checkVehicleName(): 
     # enter vehicle name
    vehicleName = input("Please Enter the full Vehicle name: ")
    if vehicleName in authorizedVehicles:
        print(f"{vehicleName} is an authorized vehicle")
    else: 
        print(f"{vehicleName} is not an authorized vehicle, if you" \
               "received this in error please check the spelling"
               "and try again")
          
# create def for ADD vehicleName
def addVehicleName(): 
    # global authorizedVehicles
    addName = input("Please Enter the full Vehicle" \
    "name you would like to add: ")
    # enter new vehicleName
    vehicleNameFileWrite(addName)
    # print authorizedVehicles list with new vehicles added
    print(f'You have added "{addName}" as an authorized vehicle')

# create def for DELETE vehicleName
def deleteVehicleName(): 
    # deleted global authorizedVehicles
    # global authorizedVehicles
    # enter vehicleName to remove
    deleteName = input("Please Enter the full Vehicle name you would" \
    " like to REMOVE: ")
    # print "Are you sure you want to remove "Nissan Titan" from the Authorized Vehicles List?"
    confirmName = input(f'Are you sure you want to remove' \
                        f'"{deleteName}" from the Authorized Vehicles List?')
    # if true, do this
    if(confirmName == "yes"): 
        if deleteName in authorizedVehicles: 
            authorizedVehicles.remove(deleteName)
            print(f'You have REMOVED "{deleteName}" as an authorized vehicle')

# write the vehileNameFile
def vehicleNameFileWrite(vehicleName): 
    with open("vehicles.txt", "w") as file: 
        file.write(vehicleName + "\n")

# read/return vehicleNameFile
# def vehicleNameReturn(): 


# final onLoad - prints what is shown in onLoad def function
onLoad()

