## 2021041047 허정윤

numStr, ch='', ''
c, i = 0, 0

if __name__ == '__main__':
    numStr = input('숫자를 여러개 입력하세요: ')
    print('')
    while True:
        ch = numStr[i]
        for c in range(0, int(ch)):
            print('\u2665', end='')
        print('')
        
        i+=1
        
        if i>len(numStr)-1:
            break
