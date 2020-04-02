#list는 대괄호로 묶으면 된다.
days = ["mon", "tue", "wed", "thur", "fri", "sat", "sun"]
print(days[2])
date = ["1","2","3","4","5","6","7","8","9","10","11"]#""을 쓰면 string으로 저장이 된다
print(len(date))
print(type(date[0]))#str
days.insert(2,"ddd")#삽입
print(days)
num = [1,2,3,4,5,6,7,8,9,0]# int타입으로 저장
print(num)
print(type(num))#타입출력
print(type(num[0]))#int
date.reverse()#뒤바꿈
print(date)
a= [[0,1,2], [3,4,5], "사과", 3, True]# 리스트 안에 리스트 넣는거 가능
print(a)# [[0,1,2], [3,4,5], "사과", 3, True]
print(a[0]) #[0,1,2]
print(a[0][1])#1
print(a[-1])#True
print(a[:2])#슬라이싱 가능# [[0, 1, 2], [3, 4, 5]]
word = ["문자열"]#
print(word[0])#문자열
print(word[0][0])#문
k=[1,2,3]#
n=[4,5,6]
j=k+n
print(j)# 리스트는 +로연결이 가능하다 *도 가능 [1, 2, 3, 4, 5, 6]
print(1 in k, 10 not in k) #True True
