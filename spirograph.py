import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.hideturtle()
screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
tim.pensize(1.4)
turtle.colormode(255)
tim.speed('fastest')

pen = Turtle()
pen.pensize(1.2)


def hex_spiral():
    colors = ['turquoise', 'blue', 'teal', 'navy']
    for i in range(180):
        tim.pencolor(colors[i % 4])
        tim.width(i / 100 + 1)
        tim.forward(i)
        tim.left(59)


def color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors


def circular():
    for _ in range(72):
        tim.color(color_gen())
        tim.circle(100)
        tim.left(5)


def hex_flower():
    angle = 360 / 6
    tim.penup()
    tim.goto(30, 100)
    tim.pendown()
    for _ in range(6):
        tim.color(color_gen())
        for i in range(5, 100):
            tim.forward(i)
            tim.right(angle)


def switch(choice):
    if choice == '1' or choice == 'circular':
        circular()
    elif choice == '2' or choice == 'Hexagonal Flower':
        hex_flower()
    elif choice == '3' or choice == 'Hexagonal spiral':
        hex_spiral()



user_input = screen.textinput(title='Choose Your Drawing', prompt=""
                                                                  "Enter the type of art you want to make:\n1.Circular\n2.Hexagonal Flower\n3.Hexagonal spiral").lower()
switch(user_input)

screen.exitonclick()
