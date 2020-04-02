#append(), insert(), extend(), 파괴적     비파괴적, del,pop(),remove()
a=[1,2,3]
a.append(4)#마지막에 ()안의 것을 추가한다
print(a)# [1,2,3,4]
a.insert(1,"a") #원하는 위치에 원하는 값추가
print(a) #[1, 'a', 2, 3, 4]
a.extend([5,6,7]) #뒤에 iterable(list나 연속하는 값) 추가
print(a) # [1, 'a', 2, 3, 4, 5, 6, 7]
a= a+[10] # 이렇게하면 append처럼 리스트 뒤에 10 추가, 리스트끼리 더하기 가능
print(a) # [1, 'a', 2, 3, 4, 5, 6, 7, 10]

x = "hello"
x.upper() #upper()함수 실행
print(x) # hello출력: upper()는 비파괴적 함수여서 함수에 사용된 변수를 변형하지 않는다.
i = x.upper() # 이런식으로 새로운 변수에 값을 저장하는 식으로 사용
print(i) #HELLO
#리스트의 함수들(append, insert, extend)은 대부분 파괴적
# b = a + [3,4,5] 식으로 연산자를 사용해서 리스트를 비파괴적으로 사용할수도 있다.

# 리스트를 인덱스로 제거 : 1.del연산자, 2. pop()함수
# 리스트를 값으로 제거 : remove()함수
del a[3]
print(a)#[1, 'a', 2, 4, 5, 6, 7]
del a[0:3] #범위를 지정해서 사용가능 1,a,2사라짐
print(a)#[4, 5, 6, 7]
print(a.pop(2)) # 6출력 : 제거하고 싶은 인덱스를 매개변수로 사용, pop()은 지우면서 지우는 값을 갖는다.
print(a) #[4, 5, 7]   매개변수 입력안하면 자동으로 -1들어가서 마지막꺼 삭제
a.remove(7) # 메개변수에 해당하는 값을 지움, 리스트에 같은 값이 있으면 앞에껄 지움
print(a) #[4, 5]