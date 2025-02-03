import time
from turtle import Turtle

ALIGNMENT = "center"
FONTS = ("Courier", 10, "normal")


class SetScreen(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = 3
        self.level = 1
        self.live_emoji = "💙💙💙"
        self.display()

    def display(self):
        self.clear()
        self.goto(x=-210, y=180)
        self.color("#00FF00")
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONTS)

        self.goto(x=-50, y=180)
        self.color("#00FF00")
        self.write(f"Lives: {self.live_emoji}", align=ALIGNMENT, font=FONTS)

        self.goto(x=150, y=180)
        self.color("#00FF00")
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONTS)

    def cal_score(self):
        self.score += 1
        self.display()

    def cal_level(self):
        self.level += 1
        if self.level == 3:
            self.level = 2
        self.display()

    def cal_lives(self):
        self.lives -= 1
        if self.live_emoji:  # remove one emoji per loss
            self.live_emoji = self.live_emoji[:-1]
            self.display()

        if self.lives == 0:  # display game over
            self.goto(x=0, y=0)
            self.color("#FF0000")
            self.write(f"Game Over", align=ALIGNMENT, font=("Courier", 20, "normal"))

    def game_won(self):
        self.goto(x=0, y=0)
        self.color("#FFFF00")
        self.write(f"🎉 YOU WIN! 🎉! - Your score: {self.score}", align=ALIGNMENT, font=("Courier", 20, "normal"))
