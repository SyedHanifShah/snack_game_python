from turtle import Turtle

SNACK_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_FORWARD = 20
DOWN = 270
UP = 90
LEFT = 180
RIGHT = 0


class Snack:
    def __init__(self) -> None:
        self.segment = []
        for position in SNACK_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        snack = Turtle(shape="square")
        snack.penup()
        snack.color("white")
        snack.goto(position)
        self.segment.append(snack)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for seg in range(len(self.segment) - 1, 0, -1):
            x_position = self.segment[seg - 1].xcor()
            y_position = self.segment[seg - 1].ycor()
            self.segment[seg].goto(x=x_position, y=y_position)
        self.segment[0].forward(MOVE_FORWARD)

    def up(self):
        if self.segment[0].heading() != DOWN:
            self.segment[0].setheading(UP)

    def down(self):
        if self.segment[0].heading() != UP:
            self.segment[0].setheading(DOWN)

    def left(self):
        if self.segment[0].heading() != RIGHT:
            self.segment[0].setheading(LEFT)

    def right(self):
        if self.segment[0].heading() != LEFT:
            self.segment[0].setheading(RIGHT)