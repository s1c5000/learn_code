#리스트인포
array = []
for i in range(0, 20, 2): # 0,2,4,6,8,...18
    array.append(i * i)
print(array) #[0, 4, 16, 36, 64, 100, 144, 196, 256, 324]

array2 = [i * i for i in range(0, 20, 2)] # 위와 같은 결과 출력, 리스트인포
print(array2)

array3 = [i for i in range(10) if i % 2 == 0] # 뒤에 조건도 추가 가능하다
print(array3) #[0, 2, 4, 6, 8]

output = 0
for i in range(1, 100+1): # 1~100까지
    if "{:b}".format(i).count("0") == 1: # 이진수로 변경시 0이 하나만 들어가는가
        print("{} : {:b}".format(i, i))
        output += i
print("합 : {}".format(output))

# 리스트인포로 위와같은 코드
output2 = [i for i in range(1, 100+1) if "{:b}".format(i).count("0") == 1]
print(output2)
print("합 : {}".format(sum(output2)))
