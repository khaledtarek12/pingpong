# import turtle modules
import turtle
# init screen and color and screen size
window = turtle.Screen()
window.title("Ping Pong By Khaled")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0) # control game update

# first 1 madrab
madrap1 = turtle.Turtle()
madrap1.speed(0)
madrap1.shape("square")
madrap1.color("blue")
madrap1.penup()
madrap1.goto(-350, 0)
madrap1.shapesize(stretch_wid=5, stretch_len=1)

# madras2
# second  madras
madrap2 = turtle.Turtle()
madrap2.speed(0) # control of the speed of the shape
madrap2.shape("square")
madrap2.color("red")
madrap2.penup() # stop the shape of drawing lines
madrap2.goto(350, 0) # set the position in the screen
madrap2.shapesize(stretch_wid=5, stretch_len=1)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .3
ball.dy = .3

# score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("player 1: 0 player 2: 0", align="center", font=("Courier", 24 ,"normal"))



# functions
def madrap1_up():
    y = madrap1.ycor() # bring the y position of madrap1
    y += 20
    madrap1.sety(y)

def madrap1_down():
    y = madrap1.ycor() # bring the y position of madrap1
    y -= 20
    madrap1.sety(y)

def madrap2_up():
    y = madrap2.ycor() # bring the y position of madrap2
    y += 20
    madrap2.sety(y)

def madrap2_down():
    y = madrap2.ycor() # bring the y position of madrap2
    y -= 20
    madrap2.sety(y)

# keyboard binding to control of the screen
window.listen() # tell the window to key input
window.onkeypress(madrap1_up, "w")
window.onkeypress(madrap1_down, "s")
window.onkeypress(madrap2_up, "Up")
window.onkeypress(madrap2_down, "Down")
# game Loop
while True:
    window.update() # update every screen run
    # move the ball
    ball.setx(ball.xcor() + ball.dx) # ball starts at 0 and increase 2.5 every time in the loop in x-axis
    ball.sety(ball.ycor() + ball.dy) # ball starts at 0 and increase 2.5 every time in the loop in y-axis
    # border check
    if ball.ycor() > 290: # if ball at top border
        ball.sety(290) # reset the position
        ball.dy *= -1 # reverse the direction

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("player 1: {} player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("player 1: {} player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    # prepare the madarep
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < madrap2.ycor() + 40 and ball.ycor() > madrap2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < madrap1.ycor() + 40 and ball.ycor() > madrap1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1