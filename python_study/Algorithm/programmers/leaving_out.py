'''
문제 설명
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

제한사항
마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
completion의 길이는 participant의 길이보다 1 작습니다.
참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
참가자 중에는 동명이인이 있을 수 있습니다.
'''

'''정확하기는 하나 효율성이 떨어짐

def solution(participant, completion):
    for i in completion:
        if i in participant:
            participant.remove(i)
    
    answer = participant[0]
    return answer


participant = ['mislav', 'stanko', 'mislav', 'ana']
completion = ['stanko', 'ana', 'mislav']	

print(solution(participant,completion))
'''
 

'''
# 리스트나 numpy는 주소를 참조하므로 copy()를 이용해서 복사한다.
def solution(participant, completion):
    array = participant.copy()
    for i in participant:
        if i not in completion:
            return i
        else:
            array.remove(i)
            completion.remove(i)
    return array[0]
'''

# collections의 Counter객체는 리스트안의 각 요소의 개수를 세어준다. 더하기 빼기 가능
# Counter({'josipa': 3, 'nikola': 2, 'marina': 1, 'vinko': 1, 'filipa': 1})
import collections

def solution(participant, completion):
    count = collections.Counter(participant)
    count2 = collections.Counter(completion)
    result = count - count2
    for i in result:
        return i


participant = 	["marina", "josipa", "nikola", "vinko", "filipa", 'josipa', 'josipa', "nikola"]
completion = ["josipa", "filipa", "marina", "nikola","vinko", 'josipa', "nikola"]
print(solution(participant,completion))
