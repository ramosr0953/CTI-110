# Ricardo Ramos
# September 20, 2026
# M1HW1
# Writing a Python program that uses mathematical expressions

print("-----Calculating Exponents----- ")

base = int(input("Enter an integer as the base number: "))
exponent = int(input("Enter an integer as the exponent: "))
result = base ** exponent
print(base, "raised to the power of", exponent, "is", result,"!!")

print("-----Addition and Subtraction----- ")

num1 = int(input("Enter a starting integer: "))
num2 = int(input("Enter an interger to add: "))
num3 = int(input("Enter an interger to subtract: "))

sum_result = num1 + num2
final_result = sum_result - num3

print(num1, "+", num2, "-", num3, "is equal to", final_result,)
