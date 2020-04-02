
if True:
    print("True 입니다")

if False:
    print("False 입니다")

number = input("정수 입력 : ")
number = int(number) # input은 string으로 저장되기때문에 형변환을 해줘야한다

if number > 0:
    print("양수입니다")
if number == 0:
    print("0입니다")
if number < 0:
    print("음수입니다")

import datetime
nowTime = datetime.datetime.now()

if nowTime.hour > 12:
    print("현재시각은 오후{}시 {}분 {}초 입니다".format(nowTime.hour%12, nowTime.minute, nowTime.second))
else:
    print("현재시각은 오전{}시 {}분 {}초 입니다".format(nowTime.hour,nowTime.minute,nowTime.second))

if 3 <= nowTime.month <= 5:
    print("이번달은 {}월로 봄입니다".format(nowTime.month))
elif 6 <= nowTime.month <= 8:
    print("이번달은 {}월로 여름입니다".format(nowTime.month))
elif 9 <= nowTime.month <= 11:
    print("이번달은 {}월로 가을입니다".format(nowTime.month))
else:
    print("이번달은 {}월로 겨울입니다".format(nowTime.month))

number = 0 # 나중에
if number !=0:
    #~~~~처리
    pass # 아무의미는 없지만 어떠한 코드를 넣어야 할때 사용, 보통 뼈대 잡을 때 사용한다.
else:
    #~~~~~처리
    pass


        