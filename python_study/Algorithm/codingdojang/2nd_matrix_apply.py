'''
6 6

  0   1   2   3   4   5
 19  20  21  22  23   6
 18  31  32  33  24   7
 17  30  35  34  25   8
 16  29  28  27  26   9
 15  14  13  12  11  10
위처럼 6 6이라는 입력을 주면 6 X 6 매트릭스에 나선형 회전을 한 값을 출력해야 한다.
'''
import numpy as np

array = np.zeros((6,6))
print(array)
x,y = 0#좌표

def v(n,c,d):#가로로 삽입(넣을수, 개수, 방향)
  for i in range(c,d):
    global array[][] = n
    n += 1