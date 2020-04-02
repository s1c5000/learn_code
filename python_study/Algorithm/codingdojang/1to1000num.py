'''
1~1000에서 각 숫자의 개수 구하기
예로 10 ~ 15 까지의 각 숫자의 개수를 구해보자
10 = 1, 0
11 = 1, 1
12 = 1, 2
13 = 1, 3
14 = 1, 4
15 = 1, 5
그러므로 이 경우의 답은 0:1개, 1:7개, 2:1개, 3:1개, 4:1개, 5:1개
'''

nums = [str(x) for x in range(1,1001)] # 1부터1000까지 문자열 형태로 저장
nums2 = [] 
for i in range(1000): # nums의 원소인 문자열을 뜯어서 저장
    len_num = len(nums[i])
    for j in range(len_num):
        nums2.append(nums[i][j])
for i in range(10):
    print("{}:{}개".format(i, nums2.count(str(i))), end=' ')