#소수를 구하는 식, 에라토스테네스의 체, 작은 소수부터 올라가면서 소수의 배수들은 지워나간다.

def primeNumberSieve(number):
    nums = [0]
    for i in range(1,number+1):
        nums.append(i)
        #print(nums[i])
    for i in range(2, number+1):
        if nums[i] == 0:
            continue
        for j in range(i*2, number+1, i):
            nums[j] = 0
    for i in range(2,number+1):
        if nums[i] != 0:
            print(nums[i],end=" ")

primeNumberSieve(1000000)
        