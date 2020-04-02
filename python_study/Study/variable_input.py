#python은 변수선언시 int, string, float 등 변수타입 자동으로 구분해줌
a=33 
print(a)
b = "333"
print(type(b))

input("입력") # '입력' 이 출력이되고 입력가능
print()

word = input(" 입력하시오 : ")
print(word)

print(input(" 입력하시오 : ")) #같은코드

x = input("첫번째 숫자입력 : ") #100입력
y = input("두번째 숫자입력 : ") #200입력
print(x + y) # 100200 출력됨 : input함수는 저장되는 값을 문자열로 저장한다.
print(type(x+y))

x = float(input("첫번째 숫자입력 : ")) #100입력, 수로 저장하려면 float이나 int로 타입변환을 해줘야한다
y = float(input("두번째 숫자입력 : ")) #200입력
print(x + y) 
print(type(x+y))

i=34
print(type(str(i)))