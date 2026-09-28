# Ricardo Ramos
# September 27, 2026
# P2HW2
# Assess understanding of lists

# Module List
module_1 = float(input("Enter grade for Module 1: "))
module_2 = float(input("Enter grade for Module 2: "))
module_3 = float(input("Enter grade for Module 3: "))
module_4 = float(input("Enter grade for Module 4: "))
module_5 = float(input("Enter grade for Module 5: "))
module_6 = float(input("Enter grade for Module 6: "))
print()

print("----------RESULTS----------")
# Results formula
numbers = [module_1, module_2, module_3, module_4, module_5, module_6]
lowest_grade = min(numbers)
highest_grade = max(numbers)
sum_of_grades = sum(numbers)
average = sum(numbers) / len(numbers)
# Results
print(f"{"Lowest Grade: ":20} {lowest_grade}")
print(f"{"Highest Grade: ":20} {highest_grade}")
print(f"{"Sum of Grades: ":20} {sum_of_grades}")
print(f"{"Average: ":20} {average:.2f}")
print("-------------------------------")