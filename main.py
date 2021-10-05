from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("light green")
screen.title("Snake")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()
# timer = Timer()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(.1)
    snake.move()
    screen.update()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 380 or snake.head.ycor() < -380:
        scoreboard.reset()
        snake.reset()

    for segment in snake.turtles[1:]:
        if snake.head.distance(segment) < 10:
            pass
        elif snake.head.distance(segment)< 10:
            scoreboard.reset()
            snake.reset()





screen.exitonclick()

