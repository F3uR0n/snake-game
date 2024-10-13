from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.all_nilu = []
        self.create_snake()
        self.head = self.all_nilu[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_nilu(position)

    def add_nilu(self, position):
        nilu = Turtle("square")
        nilu.color("white")
        nilu.penup()
        nilu.goto(position)
        self.all_nilu.append(nilu)

    def extend(self):
        self.add_nilu(self.all_nilu[-1].position())

    def move(self):
        for nil in range(len(self.all_nilu) - 1, 0, -1):
            xcor = self.all_nilu[nil - 1].xcor()
            ycor = self.all_nilu[nil - 1].ycor()
            self.all_nilu[nil].goto(xcor, ycor)
        self.all_nilu[0].forward(MOVE_DISTANCE)

    def snake_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def snake_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def snake_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def snake_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for nil in self.all_nilu:
            nil.goto(1000, 1000)
        self.all_nilu.clear()
        self.create_snake()
        self.head = self.all_nilu[0]
