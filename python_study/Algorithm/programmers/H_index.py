'''
H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 
위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면
 h의 최댓값이 이 과학자의 H-Index입니다.

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 
이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.
'''

citations=[3, 0, 50, 1, 12,4,9,20,17,56]
#citations=[3, 0, 6, 1, 5]
'''
def solution(citations):
    citations.sort(reverse=True)
    print(citations)

solution(citations)
'''

def solution(citations):
    citations = sorted(citations)
    if citations[-1] ==0:
        return 0
    h_index = citations[int(len(citations)/2)]
    while True:
        u_count = len([i for i in citations if i>=h_index])
        d_count = len([i for i in citations if i<=h_index])
        if h_index > u_count:
            h_index -=1
            continue
        if h_index <= u_count and h_index >= d_count:
            break
        if h_index < d_count:
            h_index +=1
            continue
    return h_index

solution(citations)
