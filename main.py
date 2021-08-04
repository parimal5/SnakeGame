from score_board import Score
from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=600)
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score = Score()

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

    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()

screen.exitonclick()
