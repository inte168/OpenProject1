## 2021041047 허정윤

import random

def getNumber(strData) :
    numStr = ''
    for ch in strData :
        if ch.isdigit() :
            numStr += ch

    return int(numStr)

data = []
i, k = 0, 0

if __name__ == '__main__' :
    for i in range(10):
        tmp = hex(random.randrange(100000))
        tmp = tmp[2:]
        data.append(tmp)

    print('정렬 전 : ', end='')
    [print(num, end= ' ') for num in data]

    for i in range(0, len(data) -1):
        for k in range(i+1, len(data)) :
            if getNumber(data[i])>getNumber(data[k]):
                data[i], data[k] = data[k], data[i]

    print('\n정렬 후 : ', end='')
    [print(num, end = ' ') for num in data]
            
    
