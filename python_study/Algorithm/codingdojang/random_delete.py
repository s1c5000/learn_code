'''
타노스는 프로그램의 균형을 위해서는 리스트의 원소 절반을 무작위로 삭제해야 한다고 믿고 있다.
타노스가 손가락을 튕겼을 때(프로그램을 실행했을 때) 입력된 리스트에서 절반의 원소를 무작위로 삭제하여 
리턴하는 인피니티 건틀렛 프로그램을 작성하시오.
(무작위 삭제이므로 입력값이 같아도 출력값이 매번 달라야 합니다)

입력 예시
[2, 3, 1, 6, 5, 7]
출력 예시 1
[2, 5, 7]
출력 예시 2
[3, 6, 5]

참고: 리스트의 원소가 홀수개일 경우 절반의 확률로 절반보다 많은 원소가 삭제되거나 절반보다 적은 원소가 삭제되어야 합니다.
(만약 리스트의 원소가 7개라면 절반의 확률로 3개 또는 4개의 원소가 삭제됨)
'''
import random
array = [2, 3, 1, 6, 5, 7]
array2 = [3,4,7,2,5,2,7]
def random_delete(a): # a는 list
    if len(a) % 2==0: # 개수가 짝수면
        for i in range(int(len(a)/2)):
            a.pop(random.randint(0,len(a)-1)) # random.randint(int a,int b) a부터 b까지(b포함) random한 수 출력
    else:
        for i in range(int(len(a)/2)+random.randint(0,1)):
            a.pop(random.randint(0,len(a)-1))
    return a
            
print(random_delete(array))
print(random_delete(array2))
