from collections import deque
dq = deque('love')
print(dq) # deque(['l', 'o', 'v', 'e'])

dq.appendleft('kkk') #요소를 하나의 원소로 추가할때, 오른쪽에 추가할때는 append()
print(dq) # deque(['kkk', 'l', 'o', 'v', 'e'])

dq.extendleft('aaa') #요소를 리스트형태로 추가할때, 오른쪽에 추가할때는 extend()
print(dq) # deque(['a', 'a', 'a', 'kkk', 'l', 'o', 'v', 'e'])

print(dq[0]) #a
print(dq.popleft())#a    왼쪽원소를 출력후 삭제, 오른쪽은 pop()
print(dq) # deque(['a', 'a', 'kkk', 'l', 'o', 'v', 'e'])