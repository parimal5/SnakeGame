from turtle import Turtle, Screen
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=600)
screen.title("My Snake Game")
screen.tracer(0)

pos = [(0, 0), (-20, 0), (-40, 0)]
snakes = []

for box in range(3):
    new_box = Turtle("square")
    new_box.color("white")
    new_box.penup()
    new_box.goto(pos[box])
    snakes.append(new_box)


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for snake in snakes:
        snake.forward(20)

screen.exitonclick()
