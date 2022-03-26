import turtle
import random

def screenClick(x, y):
    r=random.random()
    g=random.random()
    b=random.random()
    R=random.random()
    G=random.random()
    B=random.random()		#선과 거북이 색 랜덤
    angle = random.randrange(0, 360)	#각도 0~360 사이 랜덤
    t_size = random.randrange(2,8)	#크기 2~8사이 랜덤
    
    turtle.left(angle)		#먼저 각도 정해두고
    turtle.pencolor((r, g, b))          #랜덤한 rgb값 부여.
    turtle.goto(x,y)                    #클릭된 위치로 이동

    turtle.turtlesize(t_size)
    turtle.color((R,G,B))	#크기와 거북이 색 지정
    turtle.stamp()		#스탬프
##전역변수
pSize = 5
r,g,b, R,G,B = 0,0,0,0,0,0
angle=0
t_size = 0

##main
turtle.title("위치만 네 맘, 다른건 내 맘")
turtle.shape('turtle')
turtle.pensize(pSize)
turtle.pendown()
turtle.onscreenclick(screenClick, 3)

turtle.done()
