a = [1,2,3,4,5,6,7]
for element in a: # a의요소들을 순서대로 element라는 변수에 넣어서 반복한다.
    print(element)


numbers = [212,333,4,222,364,32,1,57]
for number in numbers:
    if number >= 100:
        print("100 이상의 수 {}".format(number))

list_of_list = [
    [1,2,3],
    [4,5,6,7],
    [8,9,10]
]
for a in list_of_list:
    #[1,2,3] > [4,5,6,7] > [8,9,10]
    for b in a:
        #1,2,3 // 4,5,6,7 // 8,9,10
        print(b)

nums = [1,2,3,4,5,6,7,8,9,]
output = [[], [], []]
for num in nums:
    output[(num-1)%3].append(num)
print(output)

holzzak = ["짝수", "홀수"]
for num in numbers:
    print("{}는 {} 입니다.".format(num, holzzak[num % 2]))

a = [293,443,22,143,456]
print(min(a)) #최솟값 22
print(max(a))  #최댓값 456
print(sum(a)) #합 1357
b = list(reversed(a)) # 뒤집는다. 뒤집은값을 b에 저장 reversed는 일회성 함수이다
print(b) #[456, 143, 22, 443, 293] 
print(b) #[456, 143, 22, 443, 293] b에 저장된값을 사용해서 다시사용가능
b2 = reversed(a) # 뒤집는다 
print(list(b2)) # [456, 143, 22, 443, 293]
print(list(b2)) # [] 일회성이여서 한번 사용하면 사용할 수 없다
for i,element in enumerate(a): # 현재인덱스가 몇번째인지 알려주고 값도 반환가능하다. 일회성함수이다. dict의 items()와 비슷
    print("{}번째 요소 {}".format(i,element)) #

