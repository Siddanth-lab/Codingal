def hotel_cost(nights):
    return 140*nights

def plane_ride_cost(city):
    if "Barcelona"==city:
        return 183
    elif "Madrid"==city:
        return 190
    elif "Paris"==city:
        return 250
    elif "Los Angeles"==city:
        return 700
    
def car_rental_cost(days):
    if days>=7:
        return 40*days-50
    elif days>=3:
        return 40*days-20
    else:
        40*days

def trip_cost(city,days,spending_money):
    return car_rental_cost(days),+hotel_cost(days)+plane_ride_cost(city)+spending_money

print("Cost of car rental: ", car_rental_cost(6))
print("Cost of plane ride: ",plane_ride_cost("Barcelona"))
print("Cost of hotel room: ", hotel_cost(7))
print("Total cost of the trip:",trip_cost("Los Angeles",7,500))
print(trip_cost("Barcelona",6,500))




