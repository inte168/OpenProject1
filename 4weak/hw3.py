import turtle
import random

myTurtle, tX, tY, tColor, tSize, tShape = [None] * 6
playerTurtles = []
swidth, sheight = 800, 800
cycle = 5
i, j, k = 0, 0, 0


if __name__ == "__main__":
    turtle.title('turtle list_fix')
    turtle.setup(width = swidth+50, height = sheight+50)
    turtle.screensize(swidth,sheight)

    for i in range(cycle):
        myTurtle = turtle.Turtle('turtle')
        tX = random.randrange(-swidth /2, swidth /2)
        tY = random.randrange(-sheight /2, sheight /2)
        r = random.random(); g = random.random(); b = random.random()
        tSize = random.randrange(1,100)/10
        tAngle = random.randrange(0,360)
        playerTurtles.append([myTurtle, tX, tY, tSize, r, g, b, tAngle])

    for i in range(cycle-1):
        mindex = i
        for j in range(i+1, cycle):
            if playerTurtles[mindex][3] > playerTurtles[j][3]:
                mindex = j
        playerTurtles[i], playerTurtles[mindex] = playerTurtles[mindex], playerTurtles[i]


    for tList in playerTurtles:
        
        myTurtle = tList[0]
        myTurtle.color((tList[4], tList[5], tList[6]))
        myTurtle.pencolor((tList[4], tList[5], tList[6]))
        myTurtle.turtlesize(tList[3])
        myTurtle.left(tList[7])
        myTurtle.penup()
        myTurtle.goto(tList[1], tList[2])

    turtle.penup()
    turtle.goto(playerTurtles[0][1], playerTurtles[0][2])
    for k in range(1, cycle):
        turtle.pendown()
        turtle.pencolor((playerTurtles[k][4], playerTurtles[k][5], playerTurtles[k][6]))
        turtle.goto(playerTurtles[k][1], playerTurtles[k][2])
        
    turtle.done()
