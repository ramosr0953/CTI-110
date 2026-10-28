# Ricardo Ramos
# October 27, 2026
# P4HW2
# Assess student's ability to edit and enhance exiting programs

# employee information input
employee_name = input("Enter employee name or 'done' to finish: ")

# Create accumulator variables for pay and employee count
overtimepay_total = 0
regularpay_total = 0
grosspay_total = 0
employee_count = 0

while employee_name != 'done':
    # Add employee count plus 1
    employee_count += 1
    employee_hours = float(input("How many hours did " + employee_name + " work this week?: "))
    employee_payrate = float(input("What is " + employee_name + "'s hourly pay rate?: "))

    # Calculate regular pay and check then calculate for overtime if necessary
    if employee_hours > 40:
        overtime_hours = employee_hours - 40
        overtime_pay = overtime_hours * (employee_payrate * 1.5)
        regular_pay = 40 * employee_payrate
        gross_pay = regular_pay + overtime_pay
    else:
        overtime_pay = 0
        overtime_hours = 0
        regular_pay = employee_hours * employee_payrate
        gross_pay = regular_pay

    # Add accumulator totals
    overtimepay_total += overtime_pay
    regularpay_total += regular_pay
    grosspay_total += gross_pay

    # Employee pay results
    print('---------------------------------')
    print('Employee Name:', employee_name)
    print()
    print(f"{'Hours Worked' :<20}{'Pay Rate':<20}{'Overtime Hours':<20}{'Overtime Pay':<20}{'Regular Pay':<20}{'Gross Pay':<20}")
    print('--------------------------------------------------------------------------------------------------------------')
    print(f"{employee_hours:<20}{employee_payrate:<20}{overtime_hours:<20}{overtime_pay:<20}{regular_pay:<20}{gross_pay:<20}")

    employee_name = input("Enter employee name or 'done' to finish: ")
print()
print("Total number of employees entered: ", employee_count)
print("Total amount paid for overtime: $", format(overtimepay_total, ',.2f'))
print("Total amount paid for regular pay: $", format(regularpay_total, ',.2f'))
print("Total amount paid for gross pay: $", format(grosspay_total, ',.2f'))