# Ricardo Ramos
# September 27, 2026
# P2LAB2
# Write a program that creates a dictionary

vehicles = {"Camaro":18.21, "Prius":52.36, "Model S":110, "Silverado":26}
vehicles_keys = vehicles.keys ()
print(vehicles_keys)
print()
vehicle_name = input("Enter a vehicle to see its MPG: ")
print()
vehicle_mpg = vehicles [vehicle_name]
print(f"The {vehicle_name} gets {vehicle_mpg} MPG ")
print()
miles_driven = float(input(f"How many miles will you drive the {vehicle_name}? "))
gallons_needed = miles_driven/vehicle_mpg
print()
print(f"{gallons_needed:.2f} Gallon(s) of gas are needed to drive the {vehicle_name} {miles_driven} miles ")
