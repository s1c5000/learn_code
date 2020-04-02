'''
두 개의 단어 begin, target과 단어의 집합 words가 있습니다. 
아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.

1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
2. words에 있는 단어로만 변환할 수 있습니다.
예를 들어 begin이 hit, target가 cog, words가 [hot,dot,dog,lot,log,cog]라면 
hit -> hot -> dot -> dog -> cog와 같이 4단계를 거쳐 변환할 수 있습니다.

두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때, 
최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return 하도록 solution 함수를 작성해주세요.
'''
'''
def make_dict(words):
    MD = {}
    for axis in range(len(words)):
        arr = []
        for i in range(len(words)):
            if axis == i:
                continue
            count = 0
            for j in range(len(words[0])):
                if words[axis][j] != words[i][j]:
                    count += 1
            if count == 1:
                arr.append(words[i])
        MD[words[axis]] = arr
    return(MD)
print(make_dict(words))
'''

begin="hit"
target="cog"
words=["hot", "dot", "dog", "lot", "log", "cog"] #4

def make_list(words):
    INF = 100000000
    ML = [[INF]*len(words) for i in range(len(words))]
    for axis in range(len(words)): #축
        for i in range(len(words)): # 제일 앞 요소부터 이동하며비교
            if axis == i: #비교할 대상이 자기 자신이면 0 넣음
                ML[axis][axis] = 0
                continue
            count = 0
            for j in range(len(words[0])): # 축과 비교요소를 글자별로 비교
                if words[axis][j] != words[i][j]:
                    count +=1
            if count == 1:
                ML[axis][i] = 1
    return ML

#방문하지 않은 노드중 가장 작은값의 인덱스를 반환
def get_samll(start_to_target,visit_index):
    INF = 100000000
    min = INF
    min_index = 0
    for i in range(len(start_to_target)):
        if i in visit_index:
            continue
        if start_to_target[i] < min:
            min_index = i
    return min_index

def solution(begin, target, words): # 다익스트라 사용
    if target not in words:
        return 0
    INF = 100000000
    words.insert(0,begin)
    target_index = words.index(target)
    ML = make_list(words)
    start_to_target = ML[0] # begin으로부터 각 노드 최단거리를 갱신 할거임
    visit_index = [0]

    while len(visit_index) < len(start_to_target):
        small = get_samll(start_to_target,visit_index)
        print("small :", small)
        using_update = ML[small]
        visit_index.append(small)
        #갱신될수 있는 노드 찾는다
        update_node = [i for i in range(len(using_update)) if i not in visit_index and using_update[i] != INF]
        print("update_node :", update_node)
        #갱신과정
        for i in update_node:
            if start_to_target[small] + using_update[i] < start_to_target[i]:
                start_to_target[i] = start_to_target[small] + using_update[i]
        print('visit_index :', visit_index)
        print('start_to_target :',start_to_target)
    return start_to_target[target_index]

print(solution(begin,target,words))



        

