#퀵정렬, 한 수를 기준으로 큰수와, 작은수를 구분해서 찾은뒤 위치를 바꾼다.  O(N*logN), 최악의 경우 N**2까지 간다.
#data = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
import random
data = []
for i in range(100):
    data.append(random.randrange(0,1000))
#random.shuffle(data)

number = len(data)
def quickSort(data, start, end):# start = 큰수를 찾는 시작부분, end는 작은수를 찾는 시작부분
    if start >= end: # 원소가 하나라면 return
        return
    
    key = start # 기준이되는 수
    i = start + 1 # 기준이 되는 수보다 큰 수를 오른쪽으로 나아가면서 찾는다
    j = end # 기준이 되는수 보다 작은 수를 왼쪽으로 나아가면서 찾는다.
    
    while i <= j: # 얻갈리기 전까지 반복
        while i <= end and data[i] <= data[key]: # 마지막부분까지 찾되 기준값보다 큰수가 나오면 중지
            # data[i] < data[key]로하게되면 key값과 i값이 같은수이고 얻갈리게되면 무한루프가 발생.
            i = i+ 1 
        while j > start and data[j] >= data[key]: # 끝부터 기준값(제일앞의 값)까지 찾되 작은수를 찾으면 중지 
            j = j - 1
        if i > j: # 기준값보다 큰수가 작은수 뒤에 있으면 작은수와 기준값의 위치를 바꾼다. 얻갈림, 실행후 while빠져나감
            temp = data[j]
            data[j] = data[key]
            data[key] = temp
        else: # 기준값보다 큰수가 작은수 앞에 있으면 큰수와 작은수의 위치를 바꾼다.
            temp = data[i]
            data[i] = data[j]
            data[j] = temp
    quickSort(data, start, j-1) # 처음부터 기준값의 전까지의 재귀함수
    quickSort(data, j+1, end) # 기준값 뒤부터 끝까지의 재귀함수
    # 한번 얻갈려서 기준값의 위치가 정해지면 그 기준값은 정렬이 되고 기준값 앞은 작은값, 뒤는 큰값이 된다.

quickSort(data, 0, number-1)
print(data)


data2 = [2,4,1,6,8,7,9,10,3,6]
random.shuffle(data2)
print("data2", data2)
def qs(data, start, end): # 내림차순으로 도 할 수있다.
    if start >= end:
        return
    i = start + 1
    j = end
    key = start
    while i<=j:
        while i <= end and data[i] >= data[key]: # 작은수찾으면 중지
            i += 1
        while j > start and data[j] <= data[key]: # 큰수 찾으면 중지
            j -= 1
        if i > j:
            temp = data[j]
            data[j] = data[key]
            data[key] = temp
        else:
            temp = data[i]
            data[i] = data[j]
            data[j] = temp
    qs(data2,j+1,end)
    qs(data2,start,j-1)

qs(data2,0,len(data2)-1)
print("data2",data2)


nums = [i for i in range(10)]
random.shuffle(nums)
#print(nums)
def myQuick(data, start, end):
    if start >= end:
        return
    
    i = start+1
    j = end
    key = start
    while i <= j:
        while i <= end and data[key] < data[i]:
            i +=1
        while j > start and data[key] > data[j]:
            j -=1
        if i > j:
            temp = data[j]
            data[j] = data[key]
            data[key] = temp
        else:
            temp = data[i]
            data[i]= data[j]
            data[j] = temp
    myQuick(data,start,j-1)
    myQuick(data,j+1,end)

myQuick(nums,0,9)
print("nums",nums)