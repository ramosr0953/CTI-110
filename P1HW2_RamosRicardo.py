# Ricardo Ramos
# September 20, 2026
# P1HW2
# create a program that does some basic math on numbers that are entered

print("This program calculates and displays travel expenses ")

budget = int(input("Enter Budget: "))
travel_destination = input("Enter your travel destination: ")
gas_expense = int(input("How much do you think you will spend on gas?: "))
hotel_expense = int(input("Approximately, how much will you need for accomodation/hotel?: "))
food_expense = int(input("Last, how much do you need for food?: "))

print("----------Travel Expenses----------")
print("Location:", travel_destination)
print("Intial Budget:", budget)
print("Fuel:", gas_expense)
print("Accomodation:", hotel_expense)
print("Food:", food_expense)

result1 = budget - gas_expense
result2 = result1 - hotel_expense
final_result = result2 - food_expense

print("remaining Balance:", final_result)