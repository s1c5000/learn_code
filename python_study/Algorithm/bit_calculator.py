arr1 = [22,24,29,31,23]
arr2 = [31,25,28,23,24]


def bit_calculator(array):
    for i in range(len(array)):
        array[i] = int("{:b}".format(array[i]))

def bit_calculator2(array):
    for i in range(len(array)):
        array[i] = bin(array[i])

bit_calculator(arr1)
bit_calculator(arr2)
print(arr1)
print(arr2)
print(type(arr1[0]))

arr = []

for i in range(len(arr2)):
    k = []
    for j in range(len(arr2)):
        array1=str(arr1[i])
        array2=str(arr2[i])
        if array1[j] + array2[j] == "00":
            k.append(' ')
        else:
            k.append('#')
    arr.append(''.join(k))
print(k)
print(arr)
