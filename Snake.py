from turtle import Turtle

snake_positions = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0  # Fixed the capitalization of "Right"


class Snake():
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in snake_positions:
            self.add_part(position)

    def add_part(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.snake.append(new_segment)

    def extend(self):
        last_segment = self.snake[-1]
        self.add_part(last_segment.position())



    def move(self):
        for snake_part_index in range(len(self.snake) - 1, 0, -1):
            xposition_before = self.snake[snake_part_index - 1].xcor()
            yposition_before = self.snake[snake_part_index - 1].ycor()
            self.snake[snake_part_index].goto(x=xposition_before, y=yposition_before)
        self.snake[0].forward(move_distance)

    def up(self):
        self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)  # Corrected to setheading on the head, not snake[0]

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:  # Corrected capitalization of RIGHT
            self.head.setheading(LEFT)
