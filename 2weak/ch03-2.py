str_in=''

if __name__=='__main__':
    str_in = input('문자열 입력: ')

    for  i in range(len(str_in)-1, -1, -1):     #길이-1이 마지막 index(처음 나와야하는 거), -1 이전까지, -1 간격으로
        print('%c' % str_in[i], end='')         #end=''로 반복될 때마다 개행되지 않게 설정.
