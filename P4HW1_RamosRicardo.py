# Ricardo Ramos
# October 27, 2026
# P4HW1
# Assess student's ability to edit and enhance exiting programs

# Asking for user input of scores
num_of_scores = int(input("How many scores would you like to enter?: "))
print()

# Module List
numbers = []

for i in range(num_of_scores):
    score = float(input(f"Enter score #{i +1}: "))
    while score < 0 or score > 100:
        print ("INVALID score entered!!!! Score must be between 0 and 100.")
        score = float(input(f"Enter a valid score for #{i + 1}: "))
    numbers.append(score)
print()

print("----------RESULTS----------")

# formulas for results
lowest_score = min(numbers)
numbers.remove(lowest_score)
sum_of_scores = sum(numbers)
average = sum_of_scores / len(numbers)
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F" 


# Results
print(f"{'Lowest Score: ':20} {lowest_score}")
print(f"{'Modified List: ':20} {numbers}")
print(f"{'Average: ':20} {average:.2f}")
print(f"{'Grade: ':20} {grade}")
print("-------------------------------")