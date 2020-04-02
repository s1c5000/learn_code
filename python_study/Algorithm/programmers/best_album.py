'''
스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 
노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

속한 노래가 많이 재생된 장르를 먼저 수록합니다.
장르 내에서 많이 재생된 노래를 먼저 수록합니다.
장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.

노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 
베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.
'''

genres=['classic', 'pop', 'classic', 'classic', 'pop']
plays=[500, 600, 150, 800, 2500]

def choose(array):
    max,max_index = 0,0
    result = []
    if len(array) == 1:
        return [0]
    while len(result) != 2:
        for i in range(len(array)):
            if array[i] > max:
                max = array[i]
                max_index = i
        result.append(max_index)
        array[max_index],max= 0,0
        max_index = 0
    return result

def solution(genres, plays):
    answer = []
    n_genres = list(set(genres))
    genres_index = [[0]*4 for i in range(len(n_genres))]
    print(genres_index)
    for i in range(len(n_genres)):
        index_list = []
        genres_plays = []
        for j in range(len(genres)):
            if n_genres[i] == genres[j]:
                index_list.append(j)
                genres_plays.append(plays[j])
        genres_index[i][0] = n_genres[i]
        genres_index[i][1] = index_list
        genres_index[i][2] = genres_plays
        genres_index[i][3] = sum(genres_plays)

    genres_index = sorted(genres_index, key = lambda x: -x[3])

    for i in range(len(genres_index)):
        array = choose(genres_index[i][2])
        for j in array:
            answer.append(genres_index[i][1][j])

    return answer

print(solution(genres,plays))