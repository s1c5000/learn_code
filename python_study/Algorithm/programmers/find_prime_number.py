'''
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 
흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 
종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
013은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
'''
from itertools import permutations

#numbers = "17"	#3   7 17 71 
numbers = "011" #2  11 101

def primeNumber(n): # primeNumber(len(numbers))
    arr = [i for i in range(10**(n))]
    result = []
    for i in range(2,len(arr)):
        if arr[i] == 0:
            continue
        else:
            result.append(arr[i])
            j=2
            while arr[i]*j < 10**(n):
                arr[i*j] = 0
                j += 1
    return result


def primeNumber2(n):
    arr = [i for i in range(n+1)]
    result = []
    for i in range(2,len(arr)):
        if arr[i] == 0:
            continue
        else:
            result.append(arr[i])
            for j in range(i*2,len(arr),i):
                arr[j] = 0
    print(__name__)
    return result


def solution(numbers):
    answer = 0
    permutation_list = []
    for i in range(len(numbers)):
        for perm in permutations(numbers,i+1):
            permutation_list.append(perm)
    for i in range(len(permutation_list)):
        temp = permutation_list[i]
        t = ''.join(temp)
        permutation_list[i]=int(t)
    
    permutation_list = list(set(permutation_list))
    #primeNumberList = primeNumber(len(numbers))
    maxN = max(permutation_list)
    primeNumberList = primeNumber2(maxN)
    
    for i in permutation_list:
        if i in primeNumberList:
            answer += 1
    return answer


print(solution(numbers))

