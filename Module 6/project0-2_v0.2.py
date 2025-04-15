# onLoad - will pring display menu
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
        # end menu selection and close
        if (menuSelection == '3'): 
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break

    
# displayMenu shows:
def displayMenu(): 
    print("****************")
    print("AutoCountry Vehicle Finder v0.1")
    print("****************")
    print("Please Enter the following number below from the following menu: ")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. Exit")

# create def for authorizedVehicles
def listAuthorizedVehicles(): 
    # What are the authorized vehicles
        # Ford F-150, Chevrolet Silverado, Tesla CyberTruck, Toyota Tundra, Nissan Titan
    authorizedVehicles = ["Ford F-150", "Chevrolet Silverado",
                           "Tesla CyberTruck", "Toyota Tundra", "Nissan Titan"]
    # print authorizedVehicles list
    for item in authorizedVehicles:
            print(item)

# create def for vehicleName - need to print each name individually and state if its authorized or not
def checkVehicleName(): 
    authorizedVehicles = ["Ford F-150", "Chevrolet Silverado",
                           "Tesla CyberTruck", "Toyota Tundra", "Nissan Titan"]
     # enter vehicle name
    vehicleName = input("Please Enter the full Vehicle name: ")
    if vehicleName in authorizedVehicles:
        print(f"{vehicleName} is an authorized vehicle")
    else: 
        print(f"{vehicleName} is not an authorized vehicle, if you received this in error please check the spelling and try again")
          

# final onLoad - prints what is shown in onLoad def function
onLoad()

