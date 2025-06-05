import turtle
import time
import random

screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

snake = turtle.Turtle()
snake.shape("square")
snake.color("green")
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(random.randint(-280, 280), random.randint(-280, 280))

score = 0
delay = 0.1

def goup():
    if snake.direction != "down":
        snake.direction = "up"

def godown():
    if snake.direction != "up":
        snake.direction = "down"

def goleft():
    if snake.direction != "right":
        snake.direction = "left"

def goright():
    if snake.direction != "left":
        snake.direction = "right"

def move():
    if snake.direction == "up":
        snake.sety(snake.ycor() + 20)
    elif snake.direction == "down":
        snake.sety(snake.ycor() - 20)
    elif snake.direction == "left":
        snake.setx(snake.xcor() - 20)
    elif snake.direction == "right":
        snake.setx(snake.xcor() + 20)

screen.listen()
screen.onkey(goup, "Up")
screen.onkey(godown, "Down")
screen.onkey(goleft, "Left")
screen.onkey(goright, "Right")

while True:
    screen.update()
    move()

    if snake.distance(food) < 15:
        food.goto(random.randint(-280, 280), random.randint(-280, 280))
        score += 1
        delay -= 0.005

    time.sleep(delay)

screen.mainloop()

