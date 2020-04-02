#문자열.함수(매개변수)    ->   주어.동사(목적어)
a = "{} {} {}     {}".format(1,2,3,4)
print(a) # 1 2 3     4
print("{}년 {}월 {}일 {}요일".format(2019, 12, 13, "금"))
print("Hello".upper()) #HELLO출력
print("HELLO".lower()) # hello출력
print("     공백제거    ".strip())#공백제거함수 공백제거
print("     공백제거    ".lstrip()) #좌측 공백제거
print("     공백제거    ".rstrip()) #     공백제거
print("가나다라마가나다라".find("다")) # 2출력, 찾는 문자의 순서를 반환, 없으면 -1반환
print(type("가나다라마바사".find("다")))# int
print("가나다라마가나다라".rfind("다")) #7출력, 찾는 문자를 오른쪽부터 찾음
print("가나" in "가나다라") # true출력 , 찾는 문자열이 있는지 알려줌, 없으면 false
print("10 20 30 40".split(" "))#['10', '20', '30', '40']출력,  뒤의 문자를 기준으로 문자열을 나누어줌, 리스트로 반환
print("10 20 30 40")