while 1:
    try:
        print(float(input("숫자를 입력해 주세요 : ")) **2)
        break
    except:
        pass

list_input = ["212", "323", "33", "오소리", "12"]
list_output = []
for item in list_input:
    try:
        float(item)# 이곳에서 float형으로 바꿀수없으면 예외가 발생하고 except로 넘어간다
        list_output.append(item) #예외없이 통과하면 리스트에 추가
    except:
        pass
print("{} 내부에 있던 숫자는".format(list_input))
print(list_output)

#finally 구문은 메소드안의 try except에서 return을 만나도 실행하게 된다.
def test():
    print("함수의 첫줄")
    try:
        print("try의 첫줄")
        return # 함수 내의 return이여서 바로 함수 종료되지만 finally는 실행함
         #break 만나도 finnay구문은 실행된다
        print("return 뒤의 줄")
    except:
        print("예외처리")
        return
    finally: #finally는 무조건 실행
        print("finally 구문 실행") 
    print("그냥 함수의 가장 아래줄") # 함수가 회출되어도 return때문에 실행 안됨

test()