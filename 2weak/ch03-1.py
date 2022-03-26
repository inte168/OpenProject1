import sys

if __name__ == "__main__":
    intV = 0
    floatV = 0.0
    boolV = True
    strV = ''
    listV = []
    tupleV = ()
    dicV = {}
    setV = set()
    
    print("int형 기본 크기 -->", sys.getsizeof(intV))
    print("float형 기본 크기 -->", sys.getsizeof(floatV))
    print("bool형 기본 크기 -->", sys.getsizeof(boolV))
    print("str형 기본 크기 -->", sys.getsizeof(strV))
    print("list형 기본 크기 -->", sys.getsizeof(listV))
    print("tuple형 기본 크기 -->", sys.getsizeof(tupleV))
    print("dictionary형 기본 크기 -->", sys.getsizeof(dicV))
    print("set형 기본 크기 -->", sys.getsizeof(setV))
