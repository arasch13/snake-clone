from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    """tmp"""

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.heading = 0

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
        self.head = self.segments[0]

    def add_segment(self, position):
        segment = Turtle("square")
        segment.penup()
        segment.color("black", "white")
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        for segment_nr, segment in reversed(list(enumerate(self.segments))):
            if segment_nr == 0:
                segment.setheading(self.heading)
                segment.forward(MOVE_DISTANCE)
            else:
                segment.setposition(self.segments[segment_nr - 1].position())

    def up(self):
        if self.heading != 270:
            self.heading = 90

    def down(self):
        if self.heading != 90:
            self.heading = 270

    def left(self):
        if self.heading != 0:
            self.heading = 180

    def right(self):
        if self.heading != 180:
            self.heading = 0

    def move_right(self):
        for segment_nr, segment in reversed(list(enumerate(self.segments))):
            if segment_nr == 0:
                segment.right(90)
                segment.forward(MOVE_DISTANCE)
            else:
                segment.setposition(self.segments[segment_nr - 1].position())
