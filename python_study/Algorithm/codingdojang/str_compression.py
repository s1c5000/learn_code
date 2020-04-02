'''
문자열을 입력받아서, 같은 문자가 연속적으로 반복되는 경우에 그 반복 횟수를 표시하여 문자열을 압축하기.
입력 예시: aaabbcccccca
출력 예시: a3b2c6a1
'''
word = input('입력 예시: ')
x = 0
count = 0
for i in range(len(word)):
    if word[x]==word[i]:
        count += 1
        if i == len(word)-1:
            print('{}{}'.format(word[x],count), end='')
    else:
        print('{}{}'.format(word[x],count), end='')
        x=i
        count = 1
        if i == len(word)-1:
            print('{}{}'.format(word[x],count), end='')
    
        

