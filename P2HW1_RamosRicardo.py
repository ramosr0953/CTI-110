# Ricardo Ramos
# September 27, 2026
# P2HW1
# Assess ability to edit and enhance exiting programs

print("This program calculates and displays travel expenses ")
print()
budget = float(input("Enter Budget: "))
print()
travel_destination = input("Enter your travel destination: ")
print()
gas_expense = float(input("How much do you think you will spend on gas?: "))
print()
hotel_expense = float(input("Approximately, how much will you need for accomodation/hotel?: "))
print()
food_expense = float(input("Last, how much do you need for food?: "))
print()
print("----------Travel Expenses----------")
print(f"{"Location:":20} {travel_destination}")
print(f"{"Intial Budget:":20} ${budget:.2f}")
print(f"{"Fuel:":20} ${gas_expense:.2f}")
print(f"{"Accomodation:":20} ${hotel_expense:.2f}")
print(f"{"Food:":20} ${food_expense:.2f}")
print("-----------------------------------")
print()
print()
result1 = budget - gas_expense
result2 = result1 - hotel_expense
final_result = result2 - food_expense

print(f"{"Remaining Balance:":20} ${final_result:.2f}")