from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIS = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.snake_parts = []
        self.create_snake()
        self.head = self.snake_parts[0]

    def create_snake(self):
        for position in POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake_part = Turtle("square")
        snake_part.color("white")
        snake_part.penup()
        snake_part.setpos(position)
        self.snake_parts.append(snake_part)

    def extend(self):
        """add a new segment to the snake"""
        self.add_segment(self.snake_parts[-1].position())


    def move(self):
        for idx in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[idx - 1].xcor()
            new_y = self.snake_parts[idx - 1].ycor()
            self.snake_parts[idx].goto(new_x, new_y)
        self.snake_parts[0].forward(MOVE_DIS)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
