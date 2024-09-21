import turtle
from turtle import Turtle
remain = 0

check = True
def access(actual_distance,distance,dest,t,pres,n):
    remain = distance
    screen = turtle.Screen()
    screen.bgcolor("grey")
    screen.setup(height=800,width=600)

    tur = Turtle()
    tur.hideturtle()
    tur.pensize(45)
    tur.speed(0)
    tur.color("black")
    tur.penup()
    tur.right(90)
    tur.forward(300)
    tur.write(f"   {pres}",font=("courier",40,"bold"))
    tur.pendown()
    tur.backward(600)
    tur.write(f"   {dest}",font=("courier",40,"bold"))


    car = Turtle()
    car.color("red")
    car.hideturtle()
    car.speed(0)
    car.pensize(60)
    car.shape("arrow")
    car.shapesize(8)
    car.penup()
    car.right(90)
    car.forward(300)
    car.right(180)
    car.forward(((actual_distance-distance)/actual_distance)*600)
    car.showturtle()
    car.write(f"{str(int(distance))} KM    ",font=("courier",30,"bold"),align="right")
    s2 = actual_distance/(t*60)
    def stop1():
        global remain,check
        check = False
        car.hideturtle()
        car.clear()
        print("Remain")
        return remain
    def road(d,s):
        import time
        global remain
        car.clear()
        car.hideturtle()
        print(d,s)
        if car.ycor()<300 and check == True:
            car.showturtle()
            d = d-(s2/20)
            car.write(f"{str(int(d))} KM    ",font=("courier",30,"bold"),align="right")
            car.forward(s)
            time.sleep(0.05)
            remain = d
            road(d,s)
        
    def car_distance(d,t):
        global remain,check
        check = True
        remain = d
        s = 600/(t*20*60)
        road(d,s)
        
    if n == "1":
        car_distance(distance,t)
    if n == "2":
        return stop1()

    screen.mainloop()
