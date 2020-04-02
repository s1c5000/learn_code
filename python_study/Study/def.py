#python에서 함수를 쓸때 앞에 def 붙이고 :  필요,  들여쓰기로 함수작성 들여쓰기 아니면 함수아님
def function():
    print("hello")
    print("bye")

def test(k): # 파이썬 함수의 변수로는 리스트,딕셔너리도 올 수 있다(미리 선언할 필요없다).
    for k in range(len(k)):
        print(k)
l = [1,2,3,4,5] 
d = {1:1, 2:2, 3:3}
test(l) # 리스트를 변수로호출
test(d) # 딕셔너리를 변수로 호출

function()
 # 가변매개변수는 일반적인 매개변수의 뒤에 쓰고 함수하나에에 하나만 올수 있다. 
def 함수이름(매개변수1, 매개변수2, *가변매개변수):
    print(매개변수1) # 1
    print(매개변수2) # 2
    print(가변매개변수) # 3 4 5 6 7  type = tuple

함수이름(1,2,3,4,5,6,7) # 매개변수의 수가 다르지만 가변매개변수 때문에 오류가나지않음

def print_n_times(word, n = 3): # 디폴트 매개변수, 매개변수 부분에 디폴트값을 지정할수 있다. 기본매개변수는 마지막에 적어야한다
    for i in range(n):
        print(word)
print_n_times("hello", 5)
print_n_times("hi") # 디폴트 매개변수가 있어서 매개변수 지정안하면 디폴트값으로실행

#함수 매개변수들의 순서
def 매개변수순서(일반매개변수1, 일반매개변수2, *가변매개변수, 기본매개변수1 = 10, 기본매개변수2 = 20):
    print(일반매개변수1, 일반매개변수2)
    print(가변매개변수)
    print(기본매개변수1, 기본매개변수2)

매개변수순서(1,2,3,4,5,6,7,8,) # 1 2 /(3, 4, 5, 6, 7, 8) / 10 20  뒤 수는 전무 가변매개변수로 들어간다
매개변수순서(1,2,3,4,5,6,기본매개변수1=7, 기본매개변수2=8) # 1 2 /(3, 4, 5, 6) / 7 8 가변매개변수가 먼저쓰이면
# 호출시 기본매개변수를 직접 지정해줘야한다

def mul(*values): 
    m = 1
    for i in values: #values는 가변매개변수로 호출할때 넣었던 수들이 들어있다.
        m *= i
    return m
print(mul(5,7,9,10)) # 3150
 #수열
def factorial_1(n): #n! = 1 * 2 * 3 * ...(n-1)* n
    b= 1
    for i in range(1, n+1):
        b *= i
    return b
def factorial_2(n): #n! = n * (n-1)!, 재귀함수
    if n == 0:
        return 1 # 0! = 1
    else:
        return n  * factorial_2(n-1)
print(factorial_1(0), factorial_1(4))
print(factorial_2(0), factorial_2(4))

#피보나치 수열
counter = 0 # 몇번 계산하는지 세는 변수
def f(n): # f(1)= 1, f(2) =1, f(n) = f(n-1) + f(n-2)
    global counter # 함수 외부에서 값을 가져오려면 global을 앞에 붙이고 써야한다
    counter +=1
    if n == 1 or n == 2:
        return 1
    else:
        return f(n-1) + f(n-2)
print(f(35)) #9227465 값 나오는데 오래걸림 재귀함수 문제점
print(counter) # 18454929번 계산한다. f값 구할때마다 다시계산
print(counter) # 18454929   함수로 외부값을 변경하는게 일회성이 아님을 알수있다
#memoization(메모화) 피보나치수열처럼 같은값을 반복해서 재귀함수로 구할때 저장소 역할로 사용
m = {1:1, 2:1}
counter2 = 0
def f2(n):
    global counter2
    counter2 += 1
    if n in m:
        return m[n]
    else: # else를 빼도 같은 코드이다.(조기리턴)이라고 하는데 파이썬에서 들여쓰기를 줄여줄수 있다.
        output = f2(n-1) + f2(n-2)
        m[n] = output
        return output
print(f2(100)) # 354224848179261915075 금방 나옴
print(counter2) # 197번 계산, 한번 계산한걸 dict m 에 넣어놔서 빼서 쓴다.

example = [[1, [2, 3]], 4, [5, [6, 7]], [8, 9]]
def flaten(data): # 재귀를 이용한 평탄화
    output = [] # output이라는 평탄화된 리스트가 들어갈 리스트선언
    for item in data:
        if type(item) is list: # item이 list 타입이라면
            output += flaten(item) # 재귀함수 호출
            #output.append(flaten(item)) #이렇게하면 원본값이 나옴, 왜?
        else:
            output += [item] # 리스트아니라면 item을 output에 넣음 output.append(item)와 같음
    return output

print("원본 데이터 " , example) #[[1, [2, 3]], 4, [5, [6, 7]], [8, 9]]
print("변형 데이터 ", flaten(example)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

