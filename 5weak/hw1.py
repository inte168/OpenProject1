## 2021041047 허정윤

inStr, outStr = "", ""
ch, newch = "", ""
i=0

if __name__ == '__main__':
    inStr = input('문자열 입력: ')

    for i in range(len(inStr)):
        ch = inStr[i]
        if ord(ch)>=ord('A') and ord(ch)<ord('Z') :
            newch = ch.lower()
        elif ord(ch)>=ord('a') and ord(ch)<ord('z') :
            newch = ch.upper()
        else:
            newch=ch

        outStr +=newch

    print("대소문자 변환: %s" % outStr)
