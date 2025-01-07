"""
Dec 12, 2024

Learning to make the game Pong with turtle
"""

from functools import partial
import turtle

scores = {
    "player1" : 0,
    "player2" : 0,
}

gameOver = False
victor = None

winThreshold = 5

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
paddleA = turtle.Turtle()
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(5, 1)
paddleA.turtlesize(5, 1)
paddleA.penup()
paddleA.goto(-330, 0)

# Right Paddle
paddleB = turtle.Turtle()
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(5, 1)
paddleA.turtlesize(5, 1)
paddleB.penup()
paddleB.goto(330, 0)


# Paddle movement
def moveUp(paddle):
    y = paddle.ycor()
    if y < 300:
        paddle.sety(y + 20)

def moveDown(paddle):
    y = paddle.ycor()
    if y > -300:
        paddle.sety(y - 20)


window.listen()
window.onkeypress(partial(moveUp, paddleA), 'w')
window.onkeypress(partial(moveDown, paddleA), 's')
window.onkeypress(partial(moveUp, paddleB), 'Up')
window.onkeypress(partial(moveDown, paddleB), 'Down')

print(paddleA.turtlesize())


# Balling
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("orange")
ball.penup()
ball.goto(0, 0)

# Ball speed
ball_speed = 20
ballDirectionX = ball_speed * 0.01
ballDirectionY = -ball_speed * 0.01

while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ballDirectionX)
    ball.sety(ball.ycor() + ballDirectionY)

    # Bounce up and down
    if ball.ycor() >= 300 or ball.ycor() <= -300:
        ballDirectionY *= -1

    # Bounce left and right
    if ball.xcor() >= 400 or ball.xcor() <= -400:
        ballDirectionX *= -1


    # Paddle collision
    if (ball.xcor() > 310 and ball.xcor() < 335) and (ball.ycor() < paddleB.ycor() + 50 and ball.ycor() > paddleB.ycor() - 50):
        ball.setx(310)
        ballDirectionX *= -1 

    if (ball.xcor() < -310 and ball.xcor() > -335) and (ball.ycor() < paddleA.ycor() + 50 and ball.ycor() > paddleA.ycor() - 50):
        ball.setx(-310)
        ballDirectionX *= -1 
