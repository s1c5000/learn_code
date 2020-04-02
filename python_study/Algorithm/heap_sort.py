#힙정렬, 힙을 통해 데이터를 정렬, 완전이진트리이용, 부모가 자식보다 크게 만들어서 root를 추출
#추출한 root와 가장마지막 노드의 값을 바꿈, 마지막노드는 제외후 다시 반복
import random
array = []
for i in range(1000):
    array.append(random.randrange(1,1001))
#array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
for i in range(1,len(array)): # i = 1,2,3,4,5,6,7,8,9
    c = i # c = 자식노드
    while True: # do while문과 같음
        root = int((c-1)/2) # 부모를 찾는 식, 나누어 떨어지지 않는값인 소수점아래는 버리기위해 int로 묶음, 두 자식모두 이 식으로 부모를 찾기 가능
        if array[c] > array[root]:# 자식이 부모보다 크다면 값을 바꿈
            temp = array[root]
            array[root] = array[c]
            array[c] = temp
        c = root # 부모를 자식노드로 함, 재귀적, 아래에서 위로 가며 최대값을 찾는 상향식
        if c != 0: # 가장위로 도달할때 까지 반복
            continue
        break # while문 나간 뒤  i 를 증가시킴, 9까지
for i in range(len(array)-1,0,-1): # i = 9,8,7,6,5,4,3,2,1
    root = 0
    temp = array[i] # 최대값인 root값과 가장마지막노드의 값을 바꿈 - > 오름차순으로 정렬됨
    array[i] = array[root]
    array[root] = temp
    c = 1 # 자식노드를 초기화 해준다
    while True:
        c = root * 2 + 1 # 자식을 구하는 식
        if c < i-1 and array[c] < array[c+1]: # 자식중 큰 값을 찾는다
            c += 1
        if c < i and array[c] > array[root]: # 자식값이 부모보다 크면 바꿈
            temp = array[c]
            array[c] = array[root]
            array[root] = temp
        root = c # 자식을 부모로 함 ,재귀적, 하향식
        if c < i :
            continue
        break

print(array)
sum = 0
for i in range(len(array)):
    sum = sum + array[i]
print(sum/len(array))

def heap(data,n):# 힙을 구하는 함수,  n = len(data)-1    9
    for i in range(1,n+1):
        c = i
        while True:
            root = int((c - 1)/2)
            if data[c] < data[root]: # 자식이 root값보다 작으면 바꿈
                temp = data[c]
                data[c] = data[root]
                data[root] = temp # root는 이진트리 중 최소값이 오게된다
            c = root
            if c != 0:
                continue
            break

def ch(data, n):
    temp = data[0]
    data[0] = data[n]
    data[n] = temp

data = [4,6,3,7,8,9,2,1,5,10]
random.shuffle(data)

n = len(data) - 1
for i in range(n,0,-1):
    heap(data, i) # 힙을 구해주는 함수
    ch(data, i) # root값과 마지막노드를 바꾸는 함수
print(data) #[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

