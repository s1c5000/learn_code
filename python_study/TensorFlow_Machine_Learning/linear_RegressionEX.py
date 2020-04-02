import numpy as np

raw_data = [ [1, 3], [2, 4], [3, 5], [4, 6], [5, 7] ]
x_data = []
t_data = []
 
def data_slicing(data):
    global x_data, t_data
    for i in data:
        x_data.append(i[0])
        t_data.append(i[1])

    x_data = np.array(x_data).reshape(len(data),1)
    t_data = np.array(t_data).reshape(len(data),1)
data_slicing(raw_data)

W = np.random.rand(1,1) # 난수생성 0 ~ 1 사이
b = np.random.rand(1) # 난수생성 0 ~ 1 사이

def loss_func(x, t): # 손실함수
    y = np.dot(x,W) + b # y = Wx + b 형태, 행렬의 곱으로 나타냄
    return ( np.sum( (t - y)**2 ) ) / ( len(x) )

 # 미분하는 함수, 손실함수를 미분해서 가장변화가 작은 값을 찾기위해 사용
 # 입력값에 대해 아주작은 변화에 따른 결과
def numerical_derivative(f, x):
    delta_x = 1e-4 # 0.0001 
    grad = np.zeros_like(x)
    
    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
    
    while not it.finished:
        idx = it.multi_index        
        tmp_val = x[idx]
        x[idx] = float(tmp_val) + delta_x
        fx1 = f(x) # f(x+delta_x)
        
        x[idx] = tmp_val - delta_x 
        fx2 = f(x) # f(x-delta_x)
        grad[idx] = (fx1 - fx2) / (2*delta_x)
        
        x[idx] = tmp_val 
        it.iternext()   
        
    return grad


# 손실함수 값 계산 함수
# 입력변수 x, t : numpy type
def error_val(x, t):
    y = np.dot(x,W) + b
    
    return ( np.sum( (t - y)**2 ) ) / ( len(x) )

# 학습을 마친 후, 임의의 데이터에 대해 미래 값 예측 함수
# 입력변수 x : numpy type
def predict(x):
    y = np.dot(x,W) + b
    
    return y


learning_rate = 1e-2  # 발산하는 경우, 1e-3 ~ 1e-6 등으로 바꾸어서 실행

f = lambda x : loss_func(x_data,t_data)
print("Initial error value = ", error_val(x_data, t_data), "Initial W = ", W, "\n", ", b = ", b )

for step in  range(8001):  
    W -= learning_rate * numerical_derivative(f, W)
    b -= learning_rate * numerical_derivative(f, b)
    
    if (step % 400 == 0):
        print("step = ", step, "error value = ", error_val(x_data, t_data), "W = ", W, ", b = ",b )

print(predict(43))
