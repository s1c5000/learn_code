#다차원 배열을 효과적으로 처리할 수 있도록 도와주는 도구, 기본 list보다 빠르다
import numpy as np

a = [0,1,2,4]
array = np.array(a)

print(array) # [0 1 2 4]
print(array.size) # 4
print(array.dtype) # int32
print(array.shape) # (4,)
print(array.ndim) # 1
print(array.reshape((2,2)))

array1 = np.arange(4) # 0~3배열 만들기
print(array1) # [0 1 2 3]

array2 = np.zeros((4,4), dtype=float) # 4*4 이고 값들이 0인 행렬을 만듬, dtype로 type설정 가능
print(array2)
'''
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
'''
array3 = np.ones((3,3), dtype=str) # dtype를 문자열로도 지정가능
print(array3)
print(array3.shape)  # (3, 3)

array4 = np.random.randint(0,10,(3,3)) # 0부터9까지 정수를 랜덤하게 초기화된 3*3배열 만들기
print(array4)
print()

array5 = np.random.normal(0,1,(3,3)) # 평균이 0이고 표준편차가 1인 표준정규를 띄는 배열
print(array5)
print()

print(np.concatenate([array, array1],)) # concatenate : 행렬 합치기,  1*4행렬을 합쳐서 1*8행렬 만든다, 
# [0 1 2 4 0 1 2 3], axis는 축을 의미 1은 세로축 0은 가로축

array6 = np.concatenate([array4,array5], axis = 1) # 3*3행렬 2개를 합쳐서 3*6행렬이된다. "axis = 1" 세로를 축으로 합침
print(array6)
print(array6.shape) # (3, 6)

array7 = array1.reshape((2,2)) # 1*4 행렬을 2*2 행렬로 만들어준다
print(array7)

array8 = np.arange(8).reshape(2,4) # 0부터8까지 2*4행렬로 만들라
left, right = np.split(array8, [2], axis=1) #3번째열을 기준으로 세로로 나눠라
print(left.shape) #(2, 2)
print(array8)
'''
[[0 1 2 3]
 [4 5 6 7]]'''
print(left)
'''
[[0 1]
 [4 5]]'''
print(right[1][1]) # 7

array9 = array8 * 10 # 각 원소에 10을 곱한다, 더하기 빼기 나누기 가능
print(array9)

# 서로다른 형태의 배열도 연산가능, 행을 우선으로 한다.
array10 = np.arange(4) # [0,1,2,3]
print(array8 + array10)
'''
[[ 0  2  4  6]
 [ 4  6  8 10]]
'''
# 2*4 행렬 + 1*4행렬의 덧샘시 1*4행렬의 값들이 2*4행렬의 행마다 더해진다.
# 4*4 행렬 + 4*1행렬의 경우 4*1행렬의 값들이 4*4행렬의 열마다 더해진다.

# 마스킹
array11 = np.arange(16).reshape(4,4)
print()
array12 = array11 < 10 # bool형태로 배열생성
print(array12)
'''
[[ True  True  True  True]
 [ True  True  True  True]
 [ True  True False False]
 [False False False False]]
'''

array11[array12] = 100 # 마스킹 된 배열을 사용해서 특정원소의 값들을 조작할 수 있다.
print(array11)
'''
[[100 100 100 100]
 [100 100 100 100]
 [100 100  10  11]
 [ 12  13  14  15]]
'''
print(np.max(array11)) # 최댓값 100
print(np.min(array11)) # 최솟값 10
print(np.sum(array11)) # 합 1075
print(np.mean(array11)) # 평균 67.1875

# 행과 열에 대해서도 연산이 가능
print(np.sum(array11, axis=0)) # [312 313 224 226] 가로축끼리 더한다. (열 별 합계)
print(np.mean(array11, axis= 1)) #[100.   100.    55.25  13.5 ] 세로축끼리 평균을 냄 ( 행 별 평균)

# 저장과 불러오기
array13 = np.arange(0,16).reshape(4,4)
#np.save('C:/Users/LEEMINJUN/python_study/Study/numpy_saved.npy', array13) # 단일객체 저장

result = np.load('C:/Users/LEEMINJUN/python_study/Study/numpy_saved.npy') # 단일객체 불러오기
print(result)

array14 = np.arange(5)
array15 = np.arange(7)
#np.savez('C:/Users/LEEMINJUN/python_study/Study/numpy_savez.npz', first_array = array14, second_array = array15) # 복수객체 저장
 # 복수일때 확장자는 npz를 쓰고, '이름 = 변수' 형태로 저장, 
data = np.load('C:/Users/LEEMINJUN/python_study/Study/numpy_savez.npz') # 파일을 불러온다
result1 = data['first_array'] # 파일에서 이름으로 찾아 꺼내 쓴다
result2 = data['second_array']
print(result1, result2) #[0 1 2 3 4] [0 1 2 3 4 5 6]


array16 = np.arange(10,0,-1) #[10  9  8  7  6  5  4  3  2  1]
array16.sort() # sort()함수는 기본적으로 오름차순으로 정렬을 수행한다
print(array16) # [ 1  2  3  4  5  6  7  8  9 10]
print(array16[::-1]) #[10  9  8  7  6  5  4  3  2  1] , 내림차순

array17 = np.array([[1,6,2],[9,2,7],[7,2,4]])
array17.sort(axis=0) # 가로축으로 정렬(열을 기준으로 정렬)
print(array17)
'''
[[1 2 2]
 [7 2 4]
 [9 6 7]]
'''

#균일한 간격으로 데이터 생성
array18 = np.linspace(0,10,5) # 0부터 10까지 5개의 데이터를 균일하게 생성하라
print(array18) # [ 0.   2.5  5.   7.5 10. ]

# 난수의 재연 ( 실행마다 결과 동일)
np.random.seed(9) # seed 값을 9에서 4로 바꾼뒤 다시 9로 바꿔서 출력을해보면 처음9로 실행했을때의 값이 바뀌지않고 나온다.
print(np.random.randint(0,10,(2,4)))
t = np.random.randint(0,10,(2,2))
print(t)

# numpy배열객체의 복사
array19 = np.arange(0,10)
array20 = array19 # numpy의 배열은 주소를 공유하게된다.
array20[0] = 99 # 주소가 같으므로 array19의 값도 바뀐다.
print(array19) # [99  1  2  3  4  5  6  7  8  9]

array21 = np.arange(0,10)
array22 = array21.copy() # array21의 값이 복사되서 array22에 할당
array22[0] = 99 # 주소가 달라서 array21의 값은 바뀌지않는다.
print(array21) # [0 1 2 3 4 5 6 7 8 9]

#중복원소 제거
array23 = np.array([1,1,2,2,2,4,4,4])
print(np.unique(array23)) #[1 2 4]
