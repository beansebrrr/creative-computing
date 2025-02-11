"""
Dec 12, 2024

Learning to make the game Pong with turtle
"""

import turtle

scores = {
    "player1" : 0,
    "player2" : 0,
}

gameOver = False
victor = None

winThreshold = 5
ball_speed = 20

# Pong Window
window = turtle.Screen()

window.title("Pong")
window.bgcolor("#709255")
window.setup(width=800, height=600)
window.tracer(0)

# Overlay
text = turtle.Turtle()
text.color("white")
text.penup()
text.hideturtle()
text.goto(0, 260)
text.write("Ping Pog", font=("Impact", 24), align="center")

# Overlay
text = turtle.Turtle()
text.color("white")
text.penup()
text.hideturtle()
text.goto(0, 220)
text.write("Player 1: 0 || Player 2: 0", font=16, align="center")


# West Paddle
paddleWest = turtle.Turtle()
paddleWest.speed(0)
paddleWest.shape("square")
paddleWest.color("white")
paddleWest.shapesize(stretch_len=1,stretch_wid=5)
paddleWest.penup()
paddleWest.goto(-330, 0)

# Right Paddle
paddleEast = turtle.Turtle()
paddleEast.speed(0)
paddleEast.shape("square")
paddleEast.color("white")
paddleEast.shapesize(stretch_len=1,stretch_wid=5)
paddleEast.penup()
paddleEast.goto(330, 0)

# Balling
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("orange")
ball.penup()
ball.goto(0, 0)
ballDirectionX = ball_speed * 0.01
ballDirectionY = ball_speed * 0.01


"""Paddle Movement"""

# Left
def moveUpWestPaddle():
    print("up")
    y = paddleWest.ycor()
    paddleWest.sety(y + 10)

def moveDownWestPaddle():
    print("down")
    y = paddleWest.ycor()
    paddleWest.sety(y - 10)

# Right
def moveUpEastPaddle():
    print("up")
    y = paddleEast.ycor()
    paddleEast.sety(y + 10)

def moveDownEastPaddle():
    print("down")
    y = paddleEast.ycor()
    paddleEast.sety(y - 10)


window.listen()
window.onkeypress(moveUpWestPaddle, "w")
window.onkeypress(moveDownWestPaddle, "s")
window.onkeypress(moveUpEastPaddle, "Up")
window.onkeypress(moveDownEastPaddle, "Down")


while True:
    window.update()

    # Ball movement
    ball.setx(ball.xcor() + ballDirectionX)
    ball.sety(ball.ycor() + ballDirectionY)

    # Bounce up and down
    if ball.ycor() >= 300 or ball.ycor() <= -300:
        ballDirectionY *= -1
    # Bounce left and right
    if ball.xcor() >= 400 or ball.xcor() <= -400:
        ballDirectionX *= -1

    
