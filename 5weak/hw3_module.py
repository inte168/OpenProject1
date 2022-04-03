## 2021041047 허정윤

import random
import math
from tkinter.simpledialog import *

pi = 3.14

def getString():
    retStr = ''
    retStr = askstring('문자열 입력', '거북이 쓸 문자열을 입력')
    return retStr

def getRGB():
    r, g, b = 0, 0, 0
    r = random.random()
    g = random.random()
    b = random.random()
    return(r,g,b)

def getXYAS(ang):
    far = 200-pi*ang/18
    x, y, angle, size = 0, 0, 0, 0
    x = far*math.cos(pi*ang/180)
    y = far*math.sin(pi*ang/180)
    return [x, y]
