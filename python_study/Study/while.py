#while 조건 :
num = [1,2,1,1,2,1,1,2,2,1]
while 1 in num:
    num.remove(1) #remove는 지워야할게 여러개있으면 앞에있는걸 지운다.
print(num)

i=0
while i<5:
    print(i, end=", ")
    i +=1
print()

array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
#index,temp
for i in range(10):
    min = 9999
    for j in range(i,10):
        if min > array[j]:
            min = array[j]
            index = j
    temp = array[i]
    array[i] = array[index]
    array[index] = temp
print(array)

    
