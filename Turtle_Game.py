from turtle import Turtle, Screen
import random

screen = Screen()
screen.bgcolor('black')
write_turtle = Turtle()
write_turtle.pencolor("white")
write_turtle.penup()
write_turtle.hideturtle()

screen.setup(width=600, height=600)
user_input = screen.textinput(title='Choose a Turtle',
                              prompt="What color turtle would you choose? 'Red', 'Purple', 'Green', 'Blue', 'Yellow', 'Pink'")
colors = ['red', 'purple', 'green', 'blue', 'yellow', 'pink']

x = -288
y = -100
i = 0
turtles = []
for tur_index in range(6):
    new_turtle = Turtle('turtle')
    turtles.append(new_turtle)
    new_turtle.color(colors[tur_index])
    new_turtle.penup()
    new_turtle.goto(x, y + i)
    i += 50

game_continue = False
if user_input:
    game_continue = True
while game_continue:
    for turtle in turtles:
        if turtle.xcor() > 285:
            game_continue = False
            if turtle.pencolor() == user_input:
                print("You have won the game! Congrats")
            else:
                print(f"You have lost. {turtle.pencolor().title()} turtle has won the race!")
        turtle.forward(random.randint(1, 10))

screen.listen()
screen.exitonclick()
