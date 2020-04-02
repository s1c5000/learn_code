#callback, lambda(filter, map)
def call_5(func):# 함수이름을 매개변수로 받는다
    for i in range(5):
        #콜백함수callback
        func(i)
def hello(num): # 출력만 해주는 함수
    print("hello", num)
call_5(hello) # hello 0, hello 1 .... 출력

call_5(lambda number: print("hello", number))# 람다를 써서 def hello()를 사용하지않았다. number에는 func(i)의 i가 들어간다.
# (lambda 매개변수: 리턴될 한줄짜리 코드)


def call_4(func):
    for i in range(4):
        #콜백함수callback
        func()
call_4(lambda : print("hello")) # 매개변수 없으면 넣지 않는다. 리턴될 코드만 적음

#filter()
def 짝수만(number): 
    return number % 2 == 0 # filter()함수 사용할때는 return값이 bool인것만 사용가능
a = list(range(100))#0~99리스트로 선언
b = filter(짝수만, a) # filter(function, iterable)  -> filter object, a의 값을 '짝수만'에 넣고 결과가 참이면 b에 넣는다.
print(b)#<filter object at 0x01649178> 리스트의reversed처럼 사용
for i in b:
    print(i, end=" ")# 0 2 4 6 8 10 12 14 16 18 20 22 24...
print(list(b)) #[]출력, 사용하면 비어버린다

c = filter((lambda number: number % 2 == 0), a)# lambda를 써서 위와 같은 효과 코드줄임
print(list(c)) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18...]

#map() 보통 기존의 리스트를 기반으로 새로운 리스트를 만들때 사용
def 제곱(number):
    return number * number
m = map(제곱,a)
print(m)# <map object at 0x016F9400>   map(function, iterable) -> map object
print(list(m)) #[0, 1, 4, 9, 16, 25, 36, 49...]

m2 = lambda number: number * number
print(list(map(m2,a))) # lambda를 이용한 map

num_list = [1,2,3,4,5]
#print("::".join(num_list)) 1::2::3::4::5출력이되길 예상했으나 num_list가 int형이여서 오류
print("::".join(map(str,num_list))) #1::2::3::4::5

num2 = list(range(1, 10+1))
print("홀수만 추출")
print(filter(lambda x: x%2==1,num2))#<filter object at 0x01849460>
print(list(filter(lambda x: x%2==1,num2)))
print("3이상 7미만 추출")
print(list(filter(lambda x: x>=3 and x<7,num2)))
print("제곱해서 50미만 추출")
print(list(filter(lambda x: x**2<50,num2)))