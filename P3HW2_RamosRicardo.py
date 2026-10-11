# Ricardo Ramos
# October 11, 2026
# P3HW2
# Assess student understanding of decision structures, using if/else statements

# employee information input
emp_name = input('Enter employee name: ')
emp_hours = float(input('Enter number of hours worked: '))
emp_payrate = float(input('Enter hourly pay rate: '))

# Calculate regular pay and check then calculate for overtime if necessary

if emp_hours > 40:
    overtime_hours = emp_hours - 40
    overtime_pay = overtime_hours * (emp_payrate * 1.5)
    regular_pay = 40 * emp_payrate
    gross_pay = regular_pay + overtime_pay
else:
    overtime_pay = 0
    overtime_hours = 0
    regular_pay = emp_hours * emp_payrate
    gross_pay = regular_pay

# Employee pay results
print('---------------------------------')
print('Employee Name:', emp_name)
print()
print(f"{'Hours Worked' :<20}{'Pay Rate':<20}{'Overtime Hours':<20}{'Overtime Pay':<20}{'Regular Pay':<20}{'Gross Pay':<20}")
print('--------------------------------------------------------------------------------------------------------------')
print(f"{emp_hours:<20}{emp_payrate:<20}{overtime_hours:<20}{overtime_pay:<20}{regular_pay:<20}{gross_pay:<20}")