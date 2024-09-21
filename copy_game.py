import turtle
import time
import random

screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(1600,800)


score = -1
delay = 0.25

border = turtle.Turtle()
border.speed(0)
border.hideturtle()
border.penup()
border.goto(-700,300)
border.pendown()
border.color('red')
border.pensize(8)
for i in range(2):
    border.forward(1400)
    border.right(90)
    border.forward(600)
    border.right(90)

scoring = turtle.Turtle()
scoring.hideturtle()
def scorecard():
    global score,delay
    scoring.clear()
    delay -= 0.005
    if delay < 0:
        delay = 0
    score += 1
    scoring.penup()
    scoring.goto(0,310)
    scoring.color("black")
    scoring.write(f"SCORE : {score}",align = "center",font=("vadana",50,"bold"))

scorecard()

food = turtle.Turtle()
food.color("green")
food.shape('square')
food.penup()
def fruit():
    # global old_fruit
    x = random.randint(-680,680)
    y = random.randint(-280,280)
    food.speed(0)
    food.goto(x,y)
    
    
    
fruit()

snake = turtle.Turtle()
snake.penup()
snake.color("black")
snake.shape('square')
snake.goto(0,0)
snake.direction = 'stop'



def snake_Up():
    if snake.direction != 'down':
        snake.direction = 'up'
def snake_Down():
    if snake.direction != 'up':
        snake.direction = 'down'
def snake_Right():
    if snake.direction != 'left':
        snake.direction = 'right'
def snake_Left():
    if snake.direction != 'right':
        snake.direction = 'left'
    
def snake_move(a,b):
    if snake.direction == 'up':
        y = snake.ycor()
        snake.sety(y+20)
    if snake.direction == 'down':
        y = snake.ycor()
        snake.sety(y-20)
    if snake.direction == 'left':
        x = snake.xcor()
        snake.setx(x-20)
    if snake.direction == 'right':
        x = snake.xcor()
        snake.setx(x+20)
    
screen.listen()
screen.onkeypress(snake_Up,'Up')
screen.onkeypress(snake_Down,'Down')
screen.onkeypress(snake_Left,'Left')
screen.onkeypress(snake_Right,'Right')

old_fruit = []
while True:
    screen.update()
    if snake.distance(food)<20:
        scorecard()
        fruit()
        new_fruit = turtle.Turtle()
        new_fruit.penup()
        new_fruit.speed(0)
        new_fruit.shape("square")
        new_fruit.color("green")
        old_fruit.append(new_fruit)
   
    

    for i in range(len(old_fruit)-1,0,-1):
        a = old_fruit[i-1].xcor()
        b = old_fruit[i-1].ycor()
        old_fruit[i].goto(a,b)

    if len(old_fruit)>0:
        a = snake.xcor()
        b = snake.ycor()
        old_fruit[0].goto(a,b)
   
    if snake.xcor()<-700:
    
        y = snake.ycor()
        snake.hideturtle()
        snake.goto(690,y)
        snake.showturtle()
    
    if snake.xcor()>700:
        y = snake.ycor()
        snake.hideturtle()
        snake.goto(-690,y)
        snake.showturtle()

    if snake.ycor()>300:
        x = snake.xcor()
        snake.hideturtle()
        snake.goto(x,-290)
        snake.showturtle()

    if snake.ycor()<-300:
        x = snake.xcor()
        snake.hideturtle()
        snake.goto(x,290)
        snake.showturtle()
    snake_move(snake.xcor(),snake.ycor())

    for f in old_fruit:
        if f.distance(snake) < 20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor('red')
            scoring.penup()
            scoring.goto(0,0)
            scoring.write("GAME OVER",align = 'center',font = ("courier",100,"bold"))
            scoring.goto(0,-200)
            scoring.write(f"SCORE : {score}",align = "center",font=("courier",50,"bold"))

    time.sleep(delay)
border.Terminator()
