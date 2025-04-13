# onLoad - will pring display menu
def onLoad(): 
    while(True): 
        displayMenu()
        menuSelection = input(" ")
        # print authorizedVehicle list
        if (menuSelection == '1'): 
            print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
            listAuthorizedVehicles()
        # end menu selection and close
        if (menuSelection == '2'): 
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break

    
# displayMenu shows:
def displayMenu(): 
    print("****************")
    print("AutoCountry Vehicle Finder v0.1")
    print("****************")
    print("Please Enter the following number below from the following menu: ")
    print("1. PRINT all Authorized Vehicles")
    print("2. Exit")

# create def for authorizedVehicles
def listAuthorizedVehicles(): 
    # What are the authorized vehicles
        # Ford F-150, Chevrolet Silverado, Tesla CyberTruck, Toyota Tundra, Nissan Titan
    authorizedVehicles = ["Ford F-150", "Chevrolet Silverado", "Tesla CyberTruck", "Toyota Tundra", "Nissan Titan"]
    # print authorizedVehicles list
    for item in authorizedVehicles:
            print(item)

# final onLoad - prints what is shown in onLoad def function
onLoad()

