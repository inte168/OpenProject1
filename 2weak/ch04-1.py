year = int(input("연도를 입력하세요 : "))
if ((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)):		#and or는 어차피 집합 개념이라 순서 무관.
    print("%d년은 윤년입니다" % year)
else:
    print("%d년은 윤년이 아닙니다" % year)
