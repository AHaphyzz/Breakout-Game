from turtle import Turtle

ALIGNMENT = "center"
FONTS = ("Courier", 10, "normal")


class SetScreen(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.high_score = 0
        self.score = 0
        self.lives = 3
        self.level = 1
        self.live_emoji = "💙💙💙"
        self.display()

    def display(self):
        self.clear()
        self.goto(x=-210, y=180)
        self.color("#00FF00")
        self.write(f"Your score: {self.score}", align=ALIGNMENT, font=FONTS)

        self.goto(x=-80, y=180)
        self.color("#00FF00")
        self.write(f"Lives: {self.live_emoji}", align=ALIGNMENT, font=FONTS)

        self.goto(x=50, y=180)
        self.color("#00FF00")
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONTS)

        self.goto(x=200, y=180)
        self.color("#00FF00")
        self.write(f"High score: {self.high_score}", align=ALIGNMENT, font=FONTS)

    def cal_score(self):
        self.score += 1
        self.display()

    def cal_high_score(self):
        with open("high_score.txt", "r") as file:
            try:
                with open("high_score.txt", "r"):
                    existing_high_score = file.read().strip()
                    if existing_high_score:
                        self.high_score = int(existing_high_score)
            except FileNotFoundError or ValueError:
                self.high_score = 0  # if file does not exist

        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as file:
                file.write(str(self.high_score))

        self.display()

    def cal_level(self):
        self.level += 1
        # if self.level == 3:
        #     self.level = 2
        self.display()

    def cal_lives(self):
        self.lives -= 1
        if self.live_emoji:  # remove one emoji per loss
            self.live_emoji = self.live_emoji[:-1]
            self.display()

    def game_over(self):
        if self.lives == 0:  # display game over
            self.goto(x=0, y=10)
            self.color("#FF0000")
            self.write("Game Over!", align=ALIGNMENT, font=("Courier", 20, "bold"))
            self.goto(x=0, y=-20)
            self.write(f"Your score: {self.score}", align=ALIGNMENT, font=("Courier", 20, "bold"))

    def game_won(self):
        self.goto(x=0, y=10)
        self.color("#FFFF00")
        self.write("🎉 YOU WIN! 🎉!", align=ALIGNMENT, font=("Courier", 20, "bold"))
        self.goto(x=0, y=-20)
        self.write(f"Your score: {self.score}", align=ALIGNMENT, font=("Courier", 20, "bold"))
