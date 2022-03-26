import turtle

num=0
swidth, sheight = 700,250		#화면 크기
curX, curY = 0,0			#위치 지정

if __name__ == "__main__" :
    turtle.title('binary turtle')
    turtle.shape('turtle')
    turtle.setup(width = swidth + 55, height = sheight + 55)		#처음 위치 지정
    turtle.screensize(swidth, sheight)				#화면 크기를 넣어줌.(위의 전역변수만 수정해도 크기 바뀌게)
    turtle.penup()						#이번 코드는 선을 사용하지 않음
    turtle.left(90)

    num = int(input("수를 입력하세요: "))
    binum=bin(num)						#이진법으로 바꿔줌
    curX = swidth/2						#찍을 위치는 중간에

    for i in range(len(binum) -2):				#이진수가 0bxxx형식이라 2를 빼준다.(횟수는 0~수-1로 수만큼 돌아감)
        turtle.goto(curX, curY)
        if num&1:						#1과 and가 참이면 마지막 자리(맨 오른쪽)이 1이란 의미.
            turtle.turtlesize(3)
            turtle.color('red')
        else:
            turtle.turtlesize(1.5)
            turtle.color('blue')

        turtle.stamp()
        curX -= 55
        num>>=1						#스탬프 찍고, 왼쪽으로 이동, 비트 오른쪽 이동

    turtle.done()
