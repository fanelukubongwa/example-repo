# Function that prints menu and return nothing
def options():
    """ 
    Displays list of cities the user can travel to and their
    associeted cost of flight

    Parameters: 
    takes no parameters

    Returns: 
    returns no value, function is just for display
    """

    print("OPTIONS:\n")
    print("C = Cape Town - R3000.00")
    print("D = Durban - R5000.00")
    print("J = Johannesburg - R1500.00")
    print("Q = quit.")

# functon that calculate total hotel cost for all nights
def hotel_cost(num_nights):
    """ 
    Calculates the total hotel cost for all days stayed

    Parameters: 
    num_nights (int): number of nights stayed at the hotel

    Returns: 
    int: Total hotel cost. 
    """ 
    return num_nights * 1000

# function that calculates the plane cost depending on city choosen
def plane_cost(city_flight):
     
    """ 
    evaluates which city the user wants to travel to and assigns
    the cost of the flight to the choosen city

    Parameters: 
    city_flighht (string): First charecter of the choosen city

    Returns: 
    int: cost of the flight to the chosen city. 
    """ 
    if city_flight == "C":
        cost_flight = 3000.00

    elif city_flight == "D":
        cost_flight =  5000.00
    
    else:
        cost_flight = 1500.00
    
    return cost_flight

# function that calculates total car rental cost
def car_rental(rental_days):
    """ 
    Calculates the total car rental cost for all days rented

    Parameters: 
    rental_days (int): number of days the car was rented for

    Returns: 
    int: Total car rental cost.

    """ 
    return rental_days * 500

# function that calculates total holiday cost
def holiday_cost(num_nights, city_flight, rental_days):
    """ 
    Calculates the total holiday cost including: flight, car rental and
    holiday stay for all days

    Parameters: 
    city_flighht (string): First charecter of the choosen city
    num_nights (int): number of nights stayed at the hotel
    rental_days (int): number of days the car was rented for

    Returns: 
    float: Total holiday cost.

    """ 

    hotel = float(hotel_cost(num_nights))
    plane = float(plane_cost(city_flight))
    car = float(car_rental(rental_days))
    return hotel + plane + car


# calling the function to display menu
options()

# Asking user to choose city from menu
city_flight = input("Please choose city fom the menu: ")
city_flight = city_flight.upper()

# ifelse statemnts to make sure the user makes a valid choice.
if city_flight == "D" or city_flight == "C" or city_flight == "J":
    
    # Storing name of the city according to user input
    city_name = ""

    if city_flight == "C":
        city_name = "Cape Town"
    elif city_flight == "D":
        city_name = "Durban"
    else:
        city_name = "Johannesburg"

    # Asking for more user input if user made a valid choice
    print("\nHotel priced at R1000 per night!")
    num_nights = int(input("Enter number of nights for your stay: "))
    print("\nRental car proced at R500 per day!")
    rental_days = int(input("Enter number of days for car rental: "))

    #Displaying the breakdownof the holiday
    print("\nHOLIDAY COST BREAKDOWN")
    print("City of choice: ", city_name)
    print("hotel for", num_nights, "days: R", hotel_cost(num_nights))
    print("Car rental for", rental_days, "days: R", car_rental(rental_days))

    # Printing the total cost. Using .2f for 2 decimal places
    print(f"\nThe total cost of this holiday is: R {holiday_cost(num_nights, city_flight, rental_days):.2f} \n")

# user may choose to quit from the menu
elif city_flight == "Q":
    print("Exiting the program!")

# Error message if user make an invalid choice
else:
    print("No valid choice made!")
