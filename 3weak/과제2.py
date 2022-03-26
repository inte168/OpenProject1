## 2021041047 허정윤 

import turtle
import random
import math

swidth, sheight = 300, 300

if __name__ == '__main__' :
    turtle.title('moving turtle')
    turtle.setup(width=swidth+50, height = sheight+50)
    turtle.screensize(swidth, sheight)

    t1= turtle.Turtle('turtle'); t1.color('red'); t1.penup()
    t2= turtle.Turtle('turtle'); t2.color('blue'); t2.penup()
    t3= turtle.Turtle('turtle'); t3.color('yellow'); t3.penup()

    t1.goto(0,0); t2.goto(-150, -150); t3.goto(150, 150)

    while True:
        angle = random.randrange(0,360)
        dist = random.randrange(1, 50)
        t1.left(angle); t1.forward(dist)
        angle = random.randrange(0,360)
        dist = random.randrange(1, 50)
        t2.left(angle); t2.forward(dist)
        angle = random.randrange(0,360)
        dist = random.randrange(1, 50)
        t3.left(angle); t3.forward(dist)
        
        t1X= t1.xcor(); t1Y=t1.ycor()
        t2X= t2.xcor(); t2Y=t2.ycor()
        t3X= t3.xcor(); t3Y=t3.ycor()

        ## 자꾸 거북이들이 탈주를 해서 추가함.
        if t1X>180 or t1Y>180:
            t1.goto(0,0)
        if t2X>180 or t2Y>180:
            t2.goto(0,0)
        if t3X>180 or t3Y>180:
            t3.goto(0,0)                

        if math.sqrt(((t1X- t2X) * (t1X-t2X)) + ((t1Y-t2Y)*(t1Y-t2Y)))<=20\
        or math.sqrt(((t1X- t3X) * (t1X-t3X)) + ((t1Y-t3Y)*(t1Y-t3Y)))<=20\
        or math.sqrt(((t3X- t2X) * (t3X-t2X)) + ((t3Y-t2Y)*(t3Y-t2Y)))<=20:
            t1.turtlesize(3); t2.turtlesize(3); t3.turtlesize(3)
            break

    turtle.done()
