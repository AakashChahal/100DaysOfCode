from turtle import Turtle
import time
positions = [(0, 0), (-20, 0), (-40, 0)]
dist = 20


class Snake:

    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for position in positions:
            self.create_segment(position)
            
    def create_segment(self, pos):
        new_snake_segment = Turtle(shape="square")
        new_snake_segment.color("green")
        new_snake_segment.penup()
        new_snake_segment.goto(pos)
        self.snake_segments.append(new_snake_segment)

    def extend_snake(self):
        self.create_segment(self.snake_segments[-1].position())

    def move(self):
        time.sleep(0.15)
        for i in range(len(self.snake_segments) - 1, -1, -1):
            if i == 0:
                self.snake_segments[i].fd(dist)
            else:
                self.snake_segments[i].goto(self.snake_segments[i - 1].position())

    def up(self):
        if self.head.heading() != 270:
            self.head.seth(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.seth(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.seth(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.seth(0)

    def restart(self):
        for seg in self.snake_segments:
            seg.goto(10000, 10000)
        self.snake_segments.clear()
        self.create_snake()
        self.head = self.snake_segments[0]
