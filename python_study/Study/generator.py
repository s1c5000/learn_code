#generator
#이터레이터(iterator)를 직접 만들 때 사용하는 구문
#일회성함수여서 메모리절약가능
#함수 내부에 yield 라는 키워드가 포함되면 해당함수는 generator가 된다. yeild (양보하다,생산하다)

def 함수():
    print("출력A")
    print("출력B")
    yield

제너레이터 = 함수()
print(제너레이터) #<generator object 함수 at 0x03132DB8>, print(함수())도 가능
next(제너레이터) # 실행 하고싶으면 next쓴다, next(함수())도 가능

def 함수2():
    print("출력C")
    print("출력D")
    yield 100

제너레이터2 = 함수2()
값 = next(제너레이터2)
print(값)# 출력C 출력D 100, 값도 이러한 형식으로 출력가능

def generatorEX():
    print("출력1")
    yield 1 # yield만나서 아래쪽을 실행하지 않고 넘어감 코드실행을 양보한다고 이해할것
    print("출력2")
    yield 2
    print("출력3")
    yield 3
    print("출력4")
    yield 4

제네레이터3 = generatorEX()
y = next(제네레이터3) #출력1, y에 yield의 1이 저장
print(y) #1, yield의 1 출력
print(y) #1 다시호출해도 1출력
y2 = next(제네레이터3) #출력2, y2에 yield의 2가 저장
print(y2) #2
next(제네레이터3) #출력3, 위의 출력1, 출력2 코드는 건너뛰고 출력됨
next(제네레이터3) #출력4

print()
next(generatorEX()) # 출력1, yield만나서 아래는 실행안나옴
next(generatorEX()) # 출력1, 따로 generatorEX()를 변수에 넣지 않아서 yield가 1에서 멈춤

제네레이터4 = generatorEX()
for i in 제네레이터4:  #stop iterator만날때까지 돈다
    print(i) # i 에는 yield의 값들이 들어간다. 코드만 실행하고 싶으면 pass쓰면 된다.
#출력1
#1
#출력2
#2 ...

for i in 제네레이터4: # 일회성 함수여서 실행되지 않음
    print(i)

