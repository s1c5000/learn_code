print("Hello world")

print("hello world " * 3)
print(1, 2, 3, 4, 5, 6)
print("안녕하세요\n안녕하세요\n")
print("안녕하세요\t안녕하세요")
#print("\")에러남
print("\\")
print("안녕하세요"[0])
print("안녕하세요"[1])
print("안녕하세요"[2])
print("안녕하세요"[3])
print("안녕하세요"[4])
print('안녕하세요'[-1])
print("안녕하세요"[0:3])#3은 포함하지 않는다
print("안녕하세요"[:3])
print("안녕하세요"[2:])
import datetime
now = datetime.datetime.now()
print(now)

Counter =0
for i in range(1,10):
    count = "B" + str(Counter + i)
    print( count, end=', ')