from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.title("Snake Game")
screen.tracer(0)
screen.listen()


snake = Snake()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

food = Food()
score_board = ScoreBoard()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # detect collision with the food
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        score_board.update_score()

    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        game_on = False
        score_board.game_over()

    # detect collision of snake head with th segments
    for segment in snake.snake_parts:
        if snake.head == segment:
            pass
        elif snake.head.distance(segment) < 10:
            game_om = False
            score_board.game_over()


screen.exitonclick()
