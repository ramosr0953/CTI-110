# Ricardo Ramos
# September 27, 2026
# P2LAB1
# Using a program to calculate the diameter, circumference, and area of a circle

import math

radius = float(input("What is the radius of the circle? "))
diameter = 2 * radius
print()
print (f"The diameter of the circle is {diameter}")
circumference = 2 * math.pi * radius
print()
print(f"The circumference of the circle is {circumference:.2f}\n")
area = math.pi * radius**2
print()
print(f"The area of the circle is {area:.3f}")
