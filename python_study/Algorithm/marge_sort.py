# 병합정렬, 일단 반으로나누고 나중에 합치면서 정렬, 시간복잡도 O(N * logN)

array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
sorted = []

def marge(a, m, middle, n):
    i = m
    j = middle + 1
    k = m

    while i <= middle and j <= n:
        if a[i] <= a[j]:
            sorted[k] = a[i]
            i += 1
        else:
            sorted[k] = a[j]
            j += 1
        k += 1
    
    if i > middle:
        for t in range(j,n+1):
            sorted[k] = a[t]
            k += 1
    else:
        for t in range(i,middle+1):
            sorted[k] = a[t]
            k += 1
    for t in range(m,n+1):
        a[t] = sorted[t]

def marge_Sort(a, m, n):
    if m < n:
        middle = int((m+n)/2)
        marge_Sort(a, m, middle)
        marge_Sort(a, middle+1, n)
        marge(a, m, middle, n)

marge_Sort(array, 0, len(array)-1)
print(array)