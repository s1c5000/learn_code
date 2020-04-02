'''
수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 
수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 
가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.
'''
first = [1,2,3,4,5]
second = [2,1,2,3,2,4,2,5]
third = [3,3,1,1,2,2,4,4,5,5]


#answers = [1,2,3,4,5,4,3,6,4,3,2,4,6,7,4,3,3,5,6,6,5,4,3,3,4,5,6,4,3,2,3,5,2,5,4,3]	#[1]
answers = [1,3,2,4,2]	#[1,2,3]


def solution(answers):
    a = []
    b = []
    c = []
    count = []
    cn = 0
    while len(a) < len(answers):
        a = a + first
    while len(b) < len(answers):
        b = b + second
    while len(c) < len(answers):
        c = c + third
    
    for i in range(len(answers)):
        if answers[i] == a[i]:
            cn +=1
    count.append(cn)
    cn = 0
    for i in range(len(answers)):
        if answers[i] == b[i]:
            cn +=1
    count.append(cn)
    cn = 0
    for i in range(len(answers)):
        if answers[i] == c[i]:
            cn +=1
    count.append(cn)
    cn = 0

    max_count = max(count)
    print(count)
    print(max_count)

    answer = []
    for i in range(len(count)):
        if count[i] == max_count:
            answer.append(i+1)
    print(answer)
    return answer

print(solution(answers))