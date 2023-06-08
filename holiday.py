
# Creating the functions to calculate the total costs of the hotel, flights, car and overall total

def hotel(num_nights, price_per_night):
    hotel_cost = num_nights * price_per_night
    print(f"Your hotel stay will be £{price_per_night} per night. The total cost for {num_nights} nights will be £{hotel_cost}.")
    return hotel_cost

def plane(city_flight, flight_price):
    if city_flight == "London":
        plane_cost = 400
    elif city_flight == "Manchester":
        plane_cost = 260
    elif city_flight == "Cardiff":
        plane_cost = 280
    elif city_flight == "Edinburgh":
        plane_cost = 360
    else:
        plane_cost = 340
    print(f"Your flight to {city_flight} will cost £{plane_cost}.")
    return plane_cost

def car(rental_days, daily_rental_cost = 80):
    car_rental = rental_days * daily_rental_cost
    print(f"The daily rental price for a car is £{daily_rental_cost}. You have chosen to rent your car for {rental_days} days. Your total will be £{car_rental}.")
    return car_rental

def holiday(hotel_cost, plane_cost, car_rental):
    holiday_cost = hotel_cost + plane_cost + car_rental
    print(f"Your total holiday cost will be £{holiday_cost}.")
    return holiday_cost

# A list for the city options and the dictionary with the prices for one night stay

cities = ["London", "Manchester", "Cardiff", "Edinburgh", "Glasgow"]

daily_prices = {"London" : 70,
          
          "Manchester" : 60,

          "Cardiff" : 45,

          "Edinburgh" : 80,

          "Glasgow" : 75

          }

# While loops for the users input on which city they want to visit, how many nights they want to stay and how many days they want to use the rental car

while True:
    city_flight = input("Please enter the city you will be flying to from the following options: London, Manchester, Cardiff, Edinburgh, Glasgow: ").capitalize()
    if city_flight not in cities:
        print("Oops. That is not a valid city. Please try again by entering one of the following options: London, Manchester, Cardiff, Edinburgh, Glasgow: ")
    else:
        break
        
while True:
    num_nights = int(input("Please enter the number of nights you would like to stay at the hotel. Maximum stay, 7 nights: "))
    if (num_nights < 1) or (num_nights > 7):
        print("Invalid entry. Please enter between 1 - 7 nights.")
    else:
        break

while True:
    rental_days = int(input("Please enter the number of days you would like to be hiring a rental car: "))
    if (rental_days < 0) or (rental_days > 7):
        print("Invalid entry. Please enter a number between 0 - 7.")
    else:
        break
print(f"You have chosen to fly to {city_flight}. Your stay will be for {num_nights} nights and you will be hiring the rental car for {rental_days} days.")

# Flight prices from the dictionary created earlier

price_per_night = daily_prices.get(city_flight) 

flight_price = 0
daily_rental_cost = 80

# Calling all of the functions created to summarise the cost of the entire holiday

plane_cost = plane(city_flight, flight_price)
hotel_cost = hotel(num_nights, price_per_night)
car_rental = car(rental_days, daily_rental_cost)
holiday(hotel_cost, plane_cost, car_rental)








