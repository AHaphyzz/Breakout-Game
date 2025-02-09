from turtle import Turtle


class CreateBall(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("#00FFFF")

        self.penup()
        self.goto(x=0, y=-164)
        self.move_horizontal = 10
        self.move_vertical = 10
        self.ball_speed = 0.4

    def move_refresh(self):
        steps = 3  # Number of small steps per movement to detect collisions better
        for _ in range(steps):
            new_x = self.xcor() + self.move_horizontal * self.ball_speed
            new_y = self.ycor() + self.move_vertical * self.ball_speed
            self.goto(x=new_x, y=new_y)

    # Detect collision with the wall
    def bounce_y(self):
        self.move_vertical *= -1

    def bounce_x(self):
        self.move_horizontal *= -1

    def reset_ball(self):
        self.goto(x=0, y=-164)
        self.bounce_y()
        self.ball_speed = 0.4

    def increase_speed(self):
        self.ball_speed = min(self.ball_speed + 0.02, 1.5)
