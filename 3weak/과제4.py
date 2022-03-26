##  2021041047 허정윤


import turtle

swidth, sheight = 800, 400

if __name__ == '__main__':
    turtle.title('gugudan tutle')
    turtle.shape('turtle')
    turtle.setup(width = swidth+50, height = sheight+50)
    turtle.screensize(swidth, sheight)

    turtle.penup()
    tX, tY = -500, 150
    turtle.goto(tX, tY)

    for i in range(1,10):
        for j in range(2,10):
            turtle.goto(tX +85 * j, tY-30 * i)
            gugu = str(j) + ' X ' + str(i) + ' = ' + str(j*i)
            turtle.write(gugu, font=('Arial', 12, 'bold','italic'))

            
    turtle.goto(00, -150)
    turtle.done()
