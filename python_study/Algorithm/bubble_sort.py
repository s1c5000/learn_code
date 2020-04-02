#버블정렬, 옆에있는 값을 비교해서 더 작은값을 앞으로보낸다. 뒤에서부터 큰 수가 정렬됨, O(N**2)
array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
for i in range(10):
    for j in range(10-1-i):
        if array[j] > array[j+1]:
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp
print(array)

def bubble_Sort(data):
    for i in range(len(data)):
        for j in range(len(data)-1 - i):
            if data[j] > data[j+1]:
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp

data = []
import random
for i in range(100):
    data.append(random.randrange(1,1000))
    
random.shuffle(data)
bubble_Sort(data)
print(data)
            