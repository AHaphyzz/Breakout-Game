from turtle import Screen
from paddle import MovePaddle
from ball import CreateBall
"""To-do List
- Set Interface - boundaries, color, show score, show lives
- set paddle - functionality (move horizontally with direction keys, ball bounce off in upward directions)
- set walls - functionality (ball to bounce off)
- set ball - functionality (move around, hid paddle, walls and obstacles)
- set obstacle - functionality (ball bounces off in downward directions, ball speed increase with each strike)
- score - functionality (calculate, keep and display score)
- lives - functionality (calculate number of tries left)
"""
# Game Interface
screen = Screen()
screen.setup(width=600, height=400)
screen.title("Breakout Arcade Game")
# screen.tracer(0)  # won't display turtle action

# objects
paddle = MovePaddle()
ball = CreateBall()


# control the left and right paddle movement
screen.listen()
screen.onkey(paddle.move_right, "Right")
screen.onkey(paddle.move_left, "Left")

# screen.update()  # display action after calling objects
screen.mainloop()
