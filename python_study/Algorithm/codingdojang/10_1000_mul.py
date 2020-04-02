'''
10~1000까지 각 숫자 분해하여 곱하기의 전체 합 구하기
예로, 10~15까지의 각 숫자 분해하여 곱하기의 전체 합은 다음과 같다.

10 = 1 * 0 = 0
11 = 1 * 1 = 1
12 = 1 * 2 = 2
13 = 1 * 3 = 3
14 = 1 * 4 = 4
15 = 1 * 5 = 5

그러므로, 이 경우의 답은 0+1+2+3+4+5 = 15
'''
def special_mul(i,j):
    array = []
    for t in range(i, j+1):
        t = str(t)
        mul = 1
        for k in range(len(t)):
            mul *=int(t[k])
        array.append(mul)
    return(sum(array))
    
print(special_mul(10,1000))
print(28*28)