from turtle import Turtle


class MovePaddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("#00FFFF")
        self.shapesize(stretch_wid=0.5, stretch_len=3)
        self.penup()
        self.goto(x=0, y=-180)

    def move_right(self):
        new_x = self.xcor() + 20
        self.goto(x=new_x, y=self.ycor())

    def move_left(self):
        new_x = self.xcor() - 20
        self.goto(x=new_x, y=self.ycor())

    def reset_paddle(self):
        self.goto(x=0, y=-180)
