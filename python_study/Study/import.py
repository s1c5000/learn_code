import calculator

print(calculator.cal(3,2))

import math as my_math# 임포트시 이름을 지정해서 사용할 수 있다.
print(my_math.pi)
print(my_math.sin(10))

from math import * # math의 모든 변수와 함수를 사용할때 math.~~ 안하고 그냥 사용가능

import sys
# 명령 매개변수
print(sys.argv) #터미널 실행시 python import.py 3 4 5 6 라고치면  ['import.py', '3', '4', '5', '6'] 값 출력
                #명령시 매개변수를 들여올 수 있다. 알고리즘, AI에 많이 쓰임