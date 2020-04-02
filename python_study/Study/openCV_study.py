#영상 처리와 컴퓨터 비전을 위한 오픈소스 라이브러리, openCV 는 BGR을 따른다. 
import cv2
import numpy as np

img_basic = cv2.imread('C:/Users/LEEMINJUN/python_study/Study/openCV_dog.jpg', cv2.IMREAD_COLOR) # 이미지를 읽는다. Color
cv2.imshow('Image Basic', img_basic) # 이미지를 보여준다. Image Basic은 이름
cv2.waitKey(0) # 바로종료되지않고 키 값을 입력받고 종료
cv2.imwrite('C:/Users/LEEMINJUN/python_study/Study/openCV_result1.png', img_basic)  # 저장, 경로르 절대경로로 설정가능

cv2.destroyAllWindows() # 윈도우 창들을 끄게 한다.

img_gray = cv2.cvtColor(img_basic, cv2.COLOR_BGR2GRAY) # 2는 to의 의미, 컬러였던 사진을 흑백으로 바꿔서 저장
cv2.imshow('Image Gray', img_gray) # 흑백 으로 바꾼 사진을 출력
cv2.waitKey(0) # 바로종료되지않고 키 값을 입력받고 종료
cv2.imwrite('C:/Users/LEEMINJUN/python_study/Study/openCV_result2.png', img_gray)  # 저장
    
#filtering
b_filter_i =  cv2.imread('C:/Users/LEEMINJUN/python_study/Study/openCV_result2.png',cv2.IMREAD_GRAYSCALE)
cv2.imshow('B_filter_i', b_filter_i)
cv2.waitKey(0)

# basic필터, 흐릿하게함, 
# 4*4 1/16의 값을 가지고 필터를 씌운뒤 평균값을 해당픽셀에 적용
# 필터를 수동으로 만듬
size = 4 # size가 커지면 블러효과가 커진다
kernel = np.ones((size,size),np.float32) / (size ** 2) 
print(kernel)

a_filter_i = cv2.filter2D(b_filter_i,-1,kernel) # 수동으로 만든 필터를 장착
cv2.imshow('A_filter_i',a_filter_i)
cv2.waitKey(0)


a_filter_i2 = cv2.blur(b_filter_i,(4,4)) #blur함수로 위의 필터를 자동으로 만들어준다. 블러링
cv2.imshow('A_filter_i2', a_filter_i2)
cv2.waitKey(0)


a_filter_i3 = cv2.GaussianBlur(b_filter_i,(5,5),0) # 가우시안블러, 크기가 홀수여야한다, 값커지면 블러효과 커짐
cv2.imshow('A_filter_i3',a_filter_i3)
cv2.waitKey(0)