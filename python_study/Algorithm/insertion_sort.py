#삽입정렬, 필요할때만 적절한 위치에 배치, 앞의 수들은 정렬이 되어있다고 가정, O(n**2)
#데이터가 거의 정렬된 상태라면 어떤 알고리즘보다도 빠르다
array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
for i in range(10-1):
    j=i
    while j>=0 and array[j] > array[j+1]:
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp
        j -= 1
print(array)

data = [9,4,3,5,2,8,7]
def insertion_Sort(data):
    for i in range(len(data)-1):
        j = i
        while j >= 0 and data[j] < data[j+1]: # 내림차순
            temp = data[j]
            data[j] = data[j+1]
            data[j+1] = temp
            j -= 1

insertion_Sort(data)
print(data)

for i in range(0,0,1):
    print("k")


nums = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
for i in range(10):
    for j in range(i, 0-1, -1):
        if nums[j] < nums[i]:
            nums.insert(j+1,nums[i])
            del nums[i+1]
            break

print(nums)