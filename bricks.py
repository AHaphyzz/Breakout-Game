from turtle import Turtle, Screen
import random

screen = Screen()

lis = (screen.addshape("blue_brick.gif"), screen.addshape("green_brick.gif"),
       screen.addshape("red_brick.gif"), screen.addshape("yellow_brick.gif"))
set_lis = ("blue_brick.gif", "red_brick.gif", "yellow_brick.gif", "red_brick.gif")

LEVEL_1 = [
    # top layer
    (-250, 165), (-180, 165), (-110, 165), (-40, 165), (30, 165), (100, 165), (170, 165), (240, 165),
    # bottom layer
    (-250, 135), (-180, 135), (-110, 135), (-40, 135), (30, 135), (100, 135), (170, 135), (240, 135)]

LEVEL_2 = [
    # Top triangle (original)
    (-30, 165), (30, 165),
    (-120, 145), (-60, 145), (0, 145), (60, 145), (120, 145),
    (-180, 125), (-90, 125), (-30, 125), (30, 125), (90, 125), (180, 125),
    # Bottom triangle (mirrored)
    (-120, 105), (-60, 105), (0, 105), (60, 105), (120, 105),
    (-30, 85), (30, 85)
]
OBS_COLORS = ["red4", "#FF4500", "#32CD32", "gold", "#FF1493", "#1E90FF", "#FFD700"]


class Bricks(Turtle):
    def __init__(self):
        super().__init__()
        self.cord = None
        self.all_bricks = []
        self.hideturtle()

    def brick_level_1(self):
        for pos in LEVEL_1:
            self.create_brick(pos)

    def brick_level_2(self):
        for pos in LEVEL_2:
            self.create_brick(pos)

    def create_brick(self, position):
        wall = Turtle("square")
        # wall.shape(set_lis)
        wall.shapesize(stretch_wid=1, stretch_len=3)
        wall.color(random.choice(OBS_COLORS))
        wall.penup()
        wall.goto(position)
        self.all_bricks.append(wall)

    def brick_position(self):
        return [brick.pos() for brick in self.all_bricks]
