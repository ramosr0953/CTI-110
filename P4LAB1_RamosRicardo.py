# Ricardo Ramos
# P4LAB1
# 10/25/2026
# Write a turtle graphics programs that draws a triangle and a square using loops

import turtle

win = turtle.Screen()
pen = turtle.Turtle ()

# turtle pen settings for square
pen.pensize (5)
pen.pencolor ("grey")
pen.shape ("turtle")

# shape code for square
for side in range (4):
    pen.forward (200)
    pen.right (90)

# turtle pen settings for triangle
pen.pensize (5)
pen.pencolor ("black")
pen.shape ("turtle") 

# shape code for triangle
sides = 3
while sides > 0:
    pen.forward (200)
    pen.left (120)
    sides = sides - 1

turtle.done ()