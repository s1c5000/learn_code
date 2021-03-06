'''
몬테카를로 방법의 가장 간단한 예시로는 원주율(π)의 값을 추정하는 것이다.

넓이가 1인 정사각형을 생각하자. 정사각형의 한 꼭지점을 중심으로 반지름이 1인 사분원을 
정사각형 안에 그린다. 그러면 사분원이 차지하는 넓이는 π/4가 될 것이다. 
이제, 0 <= x <= 1인 x를 임의로 가져오고, 독립적으로 0 <= y <= 1인 y를 임의로 가져온 후, 
x^2 + y^2 <= 1일 확률은 사분원이 차지하는 넓이와 같은 값인 π/4가 된다.

이 과정을 여러 번 수행하는 알고리즘을 작성하고, 원주율의 값을 추정하시오.
'''

import random
repeat = 10000000
in_circle = 0
for i in range(repeat):
    x = random.random()
    y = random.random()
    t = x**2 + y**2
    if t <= 1:
        in_circle +=1
print(in_circle/repeat*4)
