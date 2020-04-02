'''
각자 서로 다른 1~9까지 3자리 임의의 숫자를 정한 뒤 서로에게 3자리의 숫자를 불러서 결과를 확인합니다. 
그리고 그 결과를 토대로 상대가 정한 숫자를 예상한 뒤 맞힙니다.

* 숫자는 맞지만, 위치가 틀렸을 때는 볼
* 숫자와 위치가 모두 맞을 때는 스트라이크
* 숫자와 위치가 모두 틀렸을 때는 아웃
예를 들어, 아래의 경우가 있으면

A : 123
B : 1스트라이크 1볼.
A : 356
B : 1스트라이크 0볼.
A : 327
B : 2스트라이크 0볼.
A : 489
B : 0스트라이크 1볼.
이때 가능한 답은 324와 328 두 가지입니다.

질문한 세 자리의 수, 스트라이크의 수, 볼의 수를 담은 2차원 배열 baseball이 매개변수로 주어질 때, 
가능한 답의 개수를 return 하도록 solution 함수를 작성해주세요.

질문의 수는 1 이상 100 이하의 자연수입니다.
baseball의 각 행은 [세 자리의 수, 스트라이크의 수, 볼의 수] 를 담고 있습니다.

# ----------------------------------------------------------------
baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]	#2

def insert(*no_insert):
    a = [str(i) for i in range(1,10) if i not in no_insert]
    return a


def s2(number):
    arr = []
    a = insert(number[0],number[1],number[2])
    for i in a:
        arr.append(number[0]+number[1] + i)
    for i in a:
        arr.append(number[0] + i + number[2])
    for i in a:
        arr.append(i + number[1]+number[2])
    return arr
    

 

def solution(baseball):
    arr = []
    for i in baseball:
        number = str(i[0])
        s = i[1]
        b = i[2]
        if s ==3:
            return 1
        elif s == 2 :
            
    answer = 0
    return answer
'''

baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]	#2

from itertools import permutations
def all_num():
    numbers=list(range(1,10))
    all_number=list(permutations(numbers, 3))
    return all_number

def check_guess(guess,num):

    guess_num=[int(i) for i in str(guess[0])] #int->list
    guess_s=guess[1]; guess_b=guess[2]
    strike,ball=0,0


    for i in range(3):
        if guess_num[i]==num[i]:
            strike+=1
            continue
        if guess_num[i] in num:
            ball+=1

    if guess_s==strike and guess_b==ball:
        return True
    else :
        return False

def solution(baseball):
    all_numbers=all_num() #(1,2,3)~(9,8,7)

    answer=0
    for num in all_numbers:
        flag=True
        for guess in baseball:
            if check_guess(guess, num)==False:
                flag=False
        if flag==True:
            answer+=1

    return answer

solution(baseball)