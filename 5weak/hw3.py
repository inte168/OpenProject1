## 2021041047 허정윤

from hw3_module import *
import turtle

inStr=''
swidth, sheight = 500, 500
tX, tY, tAngle, tSize = [0] *4

turtle.title('거북이 글자쓰기(모듈버전)')
turtle.shape('turtle')
turtle.setup(width= swidth+50, height = sheight +50)
turtle.screensize(swidth, sheight)
turtle.penup()
turtle.speed(5)

inStr = getString()
i=0
for ch in inStr:
    angCh = 720/len(inStr)
    tX, tY = getXYAS(angCh*i)
    r, g, b = getRGB()

    turtle.goto(tX, tY)

    turtle.pencolor((r,g,b))
    turtle.write(ch, font =('맑은고딕', 20, 'bold'))
    i+=1

turtle.done()
