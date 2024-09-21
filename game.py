
import turtle
import time
import random
import tkinter as tk
def access():
   
    ## FOR BACKGROUND SCREEN
    screen = turtle.Screen()
    screen.title("Snake Game")
    screen.bgcolor('green')
    screen.setup(1600,800)
    screen.tracer()


    ## FOR DEADLINE BORDER
    border = turtle.Turtle()
    border.speed(0)
    border.penup()
    border.hideturtle()
    border.goto(-600,300)
    border.color('red')
    border.pensize(5)
    border.pendown()
    border.forward(1200)
    border.right(90)
    border.forward(600)
    border.right(90)
    border.forward(1200)
    border.right(90)
    border.forward(600)


    ## SCORECARD
    score = 0
    delay = 0.2
    scoring = turtle.Turtle()
    scoring.speed(0)
    scoring.hideturtle()
    scoring.penup()
    scoring.goto(-100,350)
    scoring.pendown()
    scoring.write(f"SCORE : {score}",align = "center",font = ("vardana",30,"bold"))


    ## SNAKE
    snake = turtle.Turtle()
    snake.speed(0)
    snake.shape('square')
    snake.color("black")
    snake.penup()
    snake.goto(0,0)
    snake.direction='stop'


    ## FRUIT
    fruit = turtle.Turtle()
    fruit.speed(0)
    fruit.shape('square')
    fruit.color('white')
    fruit.penup()
    fruit.goto(30,30)

    old_fruit = []

    def snake_go_up():
        if snake.direction != 'down':
            snake.direction = 'up'
    def snake_go_down():
        if snake.direction != 'up':
            snake.direction = 'down'
    def snake_go_right():
        if snake.direction != 'left':
            snake.direction = 'right'
    def snake_go_left():
        if snake.direction != 'right':
            snake.direction = 'left'

    def snake_move():
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

    ## KEYBOARD BINDING

    screen.listen()
    screen.onkeypress(snake_go_up,"Up")
    screen.onkeypress(snake_go_down,"Down")
    screen.onkeypress(snake_go_left,"Left")
    screen.onkeypress(snake_go_right,"Right")

    while True:
        screen.update()
        if snake.distance(fruit)<20:
            x = random.randint(-590,590)
            y = random.randint(-290,290)
            fruit.goto(x,y)
            scoring.clear()
            score += 1
            scoring.write(f"SCORE : {score}",align = "center",font = ("vardana",30,"bold"))
            delay -= 0.02
            if delay<0:
                delay = 0

            new_fruit = turtle.Turtle()
            new_fruit.speed(0)
            new_fruit.shape("square")
            new_fruit.color("white")
            new_fruit.penup()
            old_fruit.append(new_fruit)

        for i in range(len(old_fruit)-1,0,-1):
            a = old_fruit[i-1].xcor()
            b = old_fruit[i-1].ycor()

            old_fruit[i].goto(a,b)
        
        if len(old_fruit)>0:
            a = snake.xcor()
            b = snake.ycor()
            old_fruit[0].goto(a,b)
        snake_move()
        
        if snake.xcor() > 600 or snake.xcor() < -600 or snake.ycor() > 300 or snake.ycor() < -300:
            time.sleep(1)
            screen.clear()
            screen.bgcolor('red')
            scoring.goto(0,0)
            scoring.write(f"GAME OVER\nYOUR SCORE : {score}",align = "center",font = ("courier",40,"bold"))
        
        for food in old_fruit:
            if food.distance(snake) <20:
                time.sleep(1)
                screen.clear()
                screen.bgcolor("red")
                scoring.goto(0,0)
                scoring.write(f"GAME OVER\nYOUR SCORE : {score}",align = "center",font = ("courier",40,"bold"))

        time.sleep(delay)
    border.Terminator()


# root = tk.Tk()
# root.geometry("1600x800")
# root.config(bg = "green")

# label1 = tk.Label(root,text = "----Welcome to Snake Game----",bg = "green",fg = "red",font = ("classic",80,"bold"))
# label1.grid(padx= 330,pady =120)

# but1 = tk.Button(root,text="START",bg="black",fg="red",font=("classic",50,"bold"),command = game.access)
# but1.grid(padx=330,pady=120)


