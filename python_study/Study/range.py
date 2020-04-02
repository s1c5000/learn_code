# range(시작, 끝, 단계) range(0, 10, 1)->0 부터 9까지 1씩증가   
# range(시작, 끝) range(0, 10) 단계부분 생략가능, 생략하면 자동적으로 1로 함    
# range(끝) range(10) -> 시작도 생략가능 0으로 생각 -> 0부터 9까지 1씩증가
for i in range(10): 
    print(i)    
k = list(range(10)) 
print(k)    

array = [222,3434,4632,25456,5745]
for i in range(len(array)):
    print("{} : {}".format(i,array[i]))

for i in reversed(range(10)):
    print(i)

for i in range(9,-1,-1):
    print(i)    
