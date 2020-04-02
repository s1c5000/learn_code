#선택정렬, 가장작은것을 앞으로 보냄, O(N**2)
array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
#index,temp
for i in range(10):
    min = 9999
    for j in range(i,10):
        if min > array[j]:
            min = array[j]
            index = j
    temp = array[i] # 해당하는 번째에 작은 값과 위치를 바꿈
    array[i] = array[index]
    array[index] = temp
print(array)
print(min) #10
print(index) #9
print(temp) #10


count_cal = 0
count_change = 0
def selection_sort(data):
    for i in range(len(data)):
        min = 999
        for j in range(i,len(data)):
            global count_cal
            count_cal += 1
            if data[j] < min:
                min = data[j]
                index = j
                global count_change
                count_change +=1
        temp = data[i]
        data[i] = min
        data[index] = temp

k = [2,5,3,6,7,4,2,6,5]
selection_sort(k)
print(k)
print(count_cal)
print(count_change)


def selection_sort_down(data): # 내림차순
    for i in range(len(data)):
        max = 0
        for j in range(i,len(data)):
            if data[j] > max:
                max = data[j]
                index = j
        temp = data[i]
        data[i] = max
        data[index] = temp
t = [2,6,3,1,6,4,3,1,6]
selection_sort_down(t)
print(t)

number = int(input())
numbers = []
for i in range(number):
    numbers.append(int(input()))

for i in range(number):
    min = 1001
    for j in range(i,number):
        if min > numbers[j]:
            min = numbers[j]
            index = j
    temp = numbers[i]
    numbers[i] = min
    numbers[index] = temp

for t in numbers:
    print(t)

