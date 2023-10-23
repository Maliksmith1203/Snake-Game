from turtle import Screen
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard
import time
snake = Snake()
screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
food = Food()
scoreboard = Scoreboard()




screen.listen()
screen.onkey(snake.up,"Up")vc
++
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_score()

    # Detect collision with Wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        scoreboard.game_over()
    # Detect Collision with Tail
    for tail in snake.snake[1:]:  # Exclude the head from collision checking
        if snake.head.distance(tail) < 10:
            game_on = False
            scoreboard.game_over()
            break  # Exit the loop early if collision detected

screen.exitonclick()