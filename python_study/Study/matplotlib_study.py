#데이터를 시각화 할 수있도록 도와주는 라이브러리, 데이터분석, 인공지능모델의 시각화

import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3]
y = [1,2,3]
plt.plot(x, y) # x축 y축으로 그래프만듬
plt.title('My Plot')
plt.xlabel('X')
plt.ylabel('Y') 
#plt.show() # 결과가 새 창에 나타난다, show()가 없어도 출력된다.

plt.savefig('C:/Users/LEEMINJUN/python_study/Study/matplotlibs.png')

x = np.linspace(0, np.pi * 10, 500) # 0부터 pi*10 까지의 넓이에 500개의 점 균일하게 찍기
fig, axes = plt.subplots(2, 1) # 2개의 그래프가 들어가는 figure생성, subplot(행, 열)
axes[0].plot(x, np.sin(x))
axes[1].plot(x, np.cos(x))
plt.show()

x = np.arange(-9,10)
y = x **2
k = plt.plot(x,y, linestyle = ":", marker='*') # linestyle은 '-', ':', '-.', '--' 등이 쓰임
plt.show()


x = np.arange(-9, 10)
y1 = x ** 2
y2 = -x
plt.plot(x, y1, linestyle="-.", marker="*", color="red", label="y = x * x")
plt.plot(x, y2, linestyle=":", marker="o", color="blue", label="y = -x")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend(
  shadow=True,
  borderpad=1
)
plt.show()
