#5진법으로 적힌 문자열 '3212'를 10진법으로 바꾸기
print('진법변환')
num = '3212'
base = 5

#원래방식
a = 0
for i in range(len(num)): # 하나씩 접근하면서 바꾼다.
   a += int(num[i]) * base**(len(num)-i-1)
print("5진법으로 적힌 문자열 '3212'를 10진법으로 바꾸기(원래방식)", a) # 432

#int()는 진법전환을 지원, 다만 변환 할 수는 str 형태여야한다.
answer = int(num,base) #432
print('5진법3212를 10진법으로 바꿈(int()써서바꿈) :',answer)  


print('#--------------------------------------------------------------------------------------------------------')
#문자열 좌,우,가운데 정렬
print('문자열 좌,우,가운데 정렬')

s = '가나다라'
n = 19
print(s.ljust(n)) # 좌측 정렬
print(s.center(n)) # 가운데 정렬
print(s.rjust(n)) # 우측 정렬

print('#-------------------------------------------------------------------------------------------------------')
print('zip')
#zip
#zip(*iterables)는 각 iterables 의 요소들을 모으는 이터레이터를 만듭니다.
mylist = [ 1,2,3 ]
new_list = [ 40, 50, 60 ]
for i in zip(mylist, new_list):
    print (i)
'''
(1, 40)
(2, 50)
(3, 60)
'''
list1 = [1, 2, 3, 4]
list2 = [100, 120, 30, 300]
list3 = [392, 2, 33,1]
answer = []
for i, j, k in zip(list1, list2, list3):
   print( i , j , k )
'''
1 100 392
2 120 2
3 30 33
4 300 1
'''
# dict로도 응용  가능
animals = ['cat', 'dog', 'lion']
sounds = ['meow', 'woof', 'roar']
answer = dict(zip(animals, sounds)) # {'cat': 'meow', 'dog': 'woof', 'lion': 'roar'}
print(answer)

print('#-----------------------------------------------------------------------------------------------------------')
print('map')
# map에는 리스트뿐만 아니라 모든 반복 가능한 객체를 넣을 수 있다
#map
list1 = ['1', '100', '33']
list2 = list(map(int, list1))
print(list2) #[1, 100, 33]

input = [[1, 2], [3, 4], [5]]
ouput = list(map(len,input))
print(ouput) # [2, 2, 1]

print(list(map(str, range(10)))) #['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
def func(t):
    return t*2
x = { 1 : 10, 2 : 20, 3: 30 }
a=list(map(func,x))
b=list(map(func,[x[i] for i in x]))
print(a) #[2, 4, 6]
print(b) #[20, 40, 60]

print('#-----------------------------------------------------------------------------------------------------------')
print('리스트평탄화')
#2차원 리스트 평탄화
my_list = [[1, 2], [3, 4], [5, 6],[3]]
answer = sum(my_list, []) 
print(answer) #[1, 2, 3, 4, 5, 6, 3]
print([element for array in my_list for element in array]) #[1, 2, 3, 4, 5, 6, 3]

arr= [[1, 2], [3, 4], [5, 6],[3],[[1,2,3],1,2]]
def plane(arr):
    result = []
    for item in arr:
        if type(item) is list:
            result += plane(item)
        else:
            result.append(item)
    return result
print(plane(arr))

print('-------------------------------------------------------------------------------------------------')
#itertools
print('itertools')
import itertools

#곱집합
iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'
print(itertools.product(iterable1, iterable2, iterable3))
print(list(itertools.product(iterable1, iterable2, iterable3)))

pool = ['A', 'B', 'C']
#수열
print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 만들기
print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 수열 만들기
#조합
print(list(map(''.join, itertools.combinations(pool,3)))) # 3개의 원소로 조합 만들기
print(list(map(''.join, itertools.combinations(pool, 2)))) # 2개의 원소로 조합 만들기

print('----------------------------------------------------------------------------------------------------')
#collections
print('collections')

import collections
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
answer = collections.Counter(my_list)# Counter는 dict형태로 요소별 횟수 세서 반환, 횟수별 내림차순임
print(answer) #Counter({2: 7, 1: 4, 3: 3, 7: 3, 4: 2, 5: 2, 6: 2, 8: 2, 9: 2, 0: 2})
print(answer[0]) #2

import bisect
mylist = [1, 2, 3, 7, 9, 11, 33]
print(bisect.bisect(mylist, 3))

min_val = float('inf')
print(min_val > 10000000000)