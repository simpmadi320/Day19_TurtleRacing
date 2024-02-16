from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
print(user_bet)

colours = ["red", "orange", "yellow", "green", "blue", "purple"]

turtle_list = []

for i in range(len(colours)):
    turtle = Turtle()
    turtle.shape("turtle")
    turtle.color(colours[i])
    turtle.penup()
    turtle.goto(-225, -120 + 50*i)
    turtle_list.append(turtle)

is_race_on = True
while is_race_on:
    for turtle in turtle_list:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            is_race_on = False

            winning_colour = turtle.fillcolor()
            if winning_colour == user_bet:
                print(f"You won! {winning_colour} won the race")
            else:
                print(f"You lost... {winning_colour} won the race")




screen.exitonclick()