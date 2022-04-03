## 2021041047 허정윤

def base2(num):
    if num==0 | num==1:
        return str(num)
    else :
        return str(base2(num//2)) + str(num%2) 

def base8(num):
    if num<8:
        return str(num)
    else :
        return str(base8(num//8)) + str(num%8)
    
def base16(num):
    Oten = ['A', 'B', 'C', 'D', 'E', 'F']
    if num<16:
        if num<10:
            return str(num)
        else :
            return str(Oten[num-10])
    else :
        if num%16 <10:
            return str(base16(num//16)) + str(num%16)
        else:
            return str(base16(num//16)) + str(Oten[num%16-10])

if __name__ == '__main__':
    num = int(input("10진수 입력 --> "))

    print(base2(num))
    print(base8(num))
    print(base16(num))
    
