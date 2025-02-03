from turtle import Screen, Turtle
from paddle import MovePaddle
from ball import CreateBall
from bricks import Bricks
from set_screen import SetScreen
import time

# Game Interface
screen = Screen()
screen.setup(width=600, height=400)
screen.title("Breakout Arcade Game")
screen.bgcolor("#0D0D0D")
screen.tracer(0)  # won't display turtle action
breakout = Turtle()


# objects
paddle = MovePaddle()
ball = CreateBall()
bricks = Bricks()
game_screen = SetScreen()

# initializing screen with object attributes
bricks.brick_level_1()
game_screen.display()

# control the left and right paddle movement
screen.listen()
screen.onkey(paddle.move_right, "Right")
screen.onkey(paddle.move_left, "Left")

breakout.hideturtle()

game_play = True
while game_play:
    time.sleep(0.2)
    screen.update()
    ball.move_refresh()

    # save and get access to bricks to be removed from screen
    bricks_to_remove = []

    # get access to each brick from all_bricks list
    for brick in bricks.all_bricks:

        if abs(ball.ycor() - brick.ycor()) < 20 and abs(ball.xcor() - brick.xcor()) < 30:
            ball.bounce_y()
            game_screen.cal_score()
            brick.hideturtle()
            bricks_to_remove.append(brick)

            # Adjust ball bounce based on where it hits
            if ball.ycor() > brick.ycor():  # If hitting from above, bounce down
                ball.move_vertical = abs(ball.move_vertical) * -1
            else:  # If hitting from below, bounce up
                ball.move_vertical = abs(ball.move_vertical)

            break  # Prevent multiple collisions at once

    for brick in bricks_to_remove:
        bricks.all_bricks.remove(brick)

    # detect left and right wall then bounce
    if ball.xcor() > (screen.window_width() // 2 - 20) or ball.xcor() < -(screen.window_width() // 2 - 20):
        ball.bounce_x()

    # detect paddle and bounce
    if ball.distance(paddle) < 50 and ball.ycor() < -(screen.window_height() // 2 - 40) and ball.move_vertical < 0:
        ball.bounce_y()

    # detect upper walls
    if ball.ycor() > (screen.window_height() // 2 - 40):
        ball.bounce_y()

    # when ball goes beyond paddle
    if ball.ycor() < -(screen.window_height() // 2 + 10):
        paddle.reset_paddle()
        ball.reset_ball()
        game_screen.cal_lives()
        if game_screen.lives == 0:
            game_play = False

    # force the last frame update which removes the last wall
    screen.update()

    # check if there are any walls left
    if not bricks.all_bricks:
        time.sleep(0.5)
        game_screen.cal_level()

        # ensures the game stops after level 2 ends
        if game_screen.level == 2:
            bricks.brick_level_2()
            ball.reset_ball()
            paddle.reset_paddle()

        # display game_over sequence
        if not bricks.all_bricks:
            time.sleep(0.5)
            game_screen.game_won()
            ball.hideturtle()
            paddle.hideturtle()
            game_play = False

screen.exitonclick()
