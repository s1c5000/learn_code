#string = ['but','i', 'wont', 'hesitate', 'no' ,'more','no', 'more', 'it', 'cannot', 'wait', 'im', 'yours']
#print(string)

def heap(data,n): # n = len(data) -1
    for i in range(1, n+1):
        c = i
        while True:
            root = int((c-1)/2)
            if len(data[c]) > len(data[root]):
                temp = data[root]
                data[root] = data[c]
                data[c] = temp
            c = root
            if c != 0:
                continue
            break 

def ch(data,n):
    root = 0
    temp = data[root]
    data[root] = data[n]
    data[n] = temp

def same_word(data,n):
    for i in range(n+1):
        for j in range(i,n+1):
            if len(data[i]) == len(data[j]):
                if data[i] > data[j]:
                    temp = data[i]
                    data[i] = data[j]
                    data[j] = temp
                

#n = len(string) - 1 # 12
n = int(input()) -1
string = []
for i in range(n+1):
    string.append(input())

for i in range(n,0-1,-1):
    heap(string,i)
    ch(string,i)
same_word(string,n)

for i in range(n+1):
    if i>0 and string[i] == string[i-1]:
        continue
    print(string[i])


