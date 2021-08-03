from turtle import Turtle, Screen
from snake import Snake

import time

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=600)
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
