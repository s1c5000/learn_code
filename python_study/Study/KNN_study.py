# K-Nearest Neighbor
#비지도학습의 가장 간단한 예시, 자신과 가까운 데이터들를 찾아 자신을 결정하는 방식

import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob

img = cv2.imread('C:/Users/LEEMINJUN/python_study/Study/KNN_digit.png') # 5000개의 숫자글씨, 각각 500개씩
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 세로로 50줄, 가로로 100줄로 사진을 나눕니다.
cells = [np.hsplit(row, 100) for row in np.vsplit(gray, 50)] #50줄 먼저 나눈걸 100개로 나눈다.
x = np.array(cells) # x 배열로 저장
print(x.shape) # (50,100,20,20) 각 배열은 20*20px로 나뉘어진다.

# 각 (20 X 20) 크기의 사진을 한 줄(1 X 400)으로 바꿉니다.
train = x[:, :].reshape(-1, 400).astype(np.float32) # 머신러닝에서 학습시킬때 데이터를 길게 늘여서 집어넣는다
print(train.shape) # (5000, 400) 5000개의 데이터가 400이라는 크기를 가지고있다.

# 0이 500개, 1이 500개, ... 로 총 5,000개가 들어가는 (1 x 5000) 배열을 만듭니다.
k = np.arange(10) # 0~9까지의 리스트
train_labels = np.repeat(k, 500)[:, np.newaxis] # k에 500회를 곱하여 0이 500개 1이 500개...
print(train_labels.shape) #(5000, 1) 5000개의 이미지가 1인지 2인지 레이블 정보를 담아준것

np.savez("C:/Users/LEEMINJUN/python_study/Study/KNN_test/trained.npz", train=train, train_labels=train_labels) # 배열을 저장


# 다음과 같이 하나씩 글자를 출력할 수 있습니다.
#plt.imshow(cv2.cvtColor(x[0,0], cv2.COLOR_GRAY2RGB))
#plt.show() # 0 사진 출력

# 다음과 같이 하나씩 글자를 저장할 수 있습니다.
i=np.random.randint(100)
print(i)
cv2.imwrite('C:/Users/LEEMINJUN/python_study/Study/KNN_test/test_0.png', x[0, i])
cv2.imwrite('C:/Users/LEEMINJUN/python_study/Study/KNN_test/test_1.png', x[5, i])
cv2.imwrite('C:/Users/LEEMINJUN/python_study/Study/KNN_test/test_2.png', x[10, i])
cv2.imwrite('C:/Users/LEEMINJUN/python_study/Study/KNN_test/test_3.png', x[15, i])
cv2.imwrite('C:/Users/LEEMINJUN/python_study/Study/KNN_test/test_4.png', x[20, i])
cv2.imwrite('C:/Users/LEEMINJUN/python_study/Study/KNN_test/test_5.png', x[25, i])
cv2.imwrite('C:/Users/LEEMINJUN/python_study/Study/KNN_test/test_6.png', x[30, i])
cv2.imwrite('C:/Users/LEEMINJUN/python_study/Study/KNN_test/test_7.png', x[35, i])
cv2.imwrite('C:/Users/LEEMINJUN/python_study/Study/KNN_test/test_8.png', x[40, i])
cv2.imwrite('C:/Users/LEEMINJUN/python_study/Study/KNN_test/test_9.png', x[45, i])

          
FILE_NAME = 'C:/Users/LEEMINJUN/python_study/Study/KNN_test/trained.npz'

# 파일로부터 학습 데이터를 불러옵니다.
def load_train_data(file_name):
  with np.load(file_name) as data:
    train = data['train']
    train_labels = data['train_labels']
  return train, train_labels

# 손 글씨 이미지를 (20 x 20) 크기로 Scaling합니다.
def resize20(image):
  img = cv2.imread(image)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  gray_resize = cv2.resize(gray, (20, 20))
  plt.imshow(cv2.cvtColor(gray_resize, cv2.COLOR_GRAY2RGB))
  plt.show()
  # 최종적으로는 (1 x 400) 크기로 반환합니다.
  return gray_resize.reshape(-1, 400).astype(np.float32)

def check(test, train, train_labels):
  knn = cv2.ml.KNearest_create()
  knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)
  # 가장 가까운 5개의 글자를 찾아, 어떤 숫자에 해당하는지 찾습니다.
  ret, result, neighbours, dist = knn.findNearest(test, k=5)
  return result

train, train_labels = load_train_data(FILE_NAME)

for file_name in glob.glob('C:/Users/LEEMINJUN/python_study/Study/KNN_test/test_*.png'):
  test = resize20(file_name)
  result = check(test, train, train_labels)
  print(result)