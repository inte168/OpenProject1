## 2021041047 허정윤 

import random

i, j=0, 0

while(True):
    d1 = random.randrange(1,7)
    d2 = random.randrange(1,7)
    d3 = random.randrange(1,7)
    d4 = random.randrange(1,7)
    d5 = random.randrange(1,7)
    d6 = random.randrange(1,7)
    
    i+=1
    
    if(d1==d2==d3==d4==d5==d6):
       break
    if not(d1==d2 or d1==d3 or d1==d4 or d1==d5 or d1==d6
           or d2==d3 or d2==d4 or d2==d5 or d2==d6
           or d3==d4 or d3==d5 or d3==d6
           or d4==d5 or d4==d6
           or d5==d6):
        j+=1
    
   
print("%d %d %d %d %d %d" % (d1,d2,d3,d4,d5,d6))
print("던진 횟수: %d" % i)
print("1-6까지 연속되게 나온 경우: %d" % j)
