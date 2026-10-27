# Ricardo Ramos
# October 26, 2026
# P4LAB2
# Test my ability to use loops to display information to users

# Ask the user to enter an integer.
# If the integer is 0 or greater, display the multiplication table for that number from 1 to 12.
# If the integer is less than 0, display a message saying negative values are not accepted.
# After each run, ask the user if they want to run the program again.
# If user enters "yes" → run again
# If user enters "no" → end program

run_again = 'yes'

while run_again != "no":
    
    user_num = int(input("Enter an Integer: "))
    if user_num >= 0: 
        for item in range (1, 13):
            print(f"{item} * {user_num} = {item * user_num}")
    else:
        print("This program does not handle negative values, please try again.")

    run_again = input("Would you like to run the program again? (yes/no): ")
print("Thank you, the program has ended.")