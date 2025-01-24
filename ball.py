from turtle import Turtle


class CreateBall(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("black")
        self.penup()
        self.goto(x=0, y=-164)