class Student:
    def __init__(self, name, age): # 생성자 self는 항상있어야하는 기본적인 매개변수로 자신을 가르킨다.
        print("객체가 생성되었습니다")
        self.name = name
        self.age = age
    def __del__(self): # 소멸자
        print("객체가 소멸되었습니다")
    def out(self): # 함수
        print(self.name, self.age) #self로 자신한테 접근 가능
    def __eq__(self,other): #자신과 비교할 대상필요 equal  ==
        print("eq( 함수)") 
    def __ne__(self,other): #not equal  !=
        print("ne( 함수)")
    def __gt__(self,other): #greater than  > (왼쪽기준임, 왼쪽이 오른쪽보다 크다)
        print("gt( 함수)")
    def __ge__(self,other): #greater than or equal  >=
        print("ge( 함수)")
    def __lt__(self,other): #less than  <
        print("lt( 함수)")
    def __le__(self,other): #less than or equal  <=
        print("le( 함수)")

student = Student("이민준", 9) #생성자를통해 객체생성
print(student.name, student.age)#이민준 9
student.out()#이민준 9
student == student # eq
student != student # ne
student > student # gt
student >= student # ge
student < student # lt
student <= student # le

class Rect:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise Exception("너비와 높이는 음수가 나올 수 없습니다")
        self.__width = width # 변수앞에 __를 쓰면 외부에서 접근할 수 없다. private
        self.__height = height
    def get_width(self): # 외부에서 접근하지못해서 get이라는 함수로 값 접근가능하게 해놓음
        return self.__width
    def set_width(self, width): # 외부에서 이 set함수를 통해 값을 변경 할 수있다.
        if width <= 0:
            raise Exception("너비와 높이는 음수가 나올 수 없습니다")
        self.__width = width # 클래스 내에서 접근이기때문에 값 설정 가능

    def get_height(self):
        return self.__height
    def set_height(self, height):
        if height <= 0:
            raise Exception("너비와 높이는 음수가 나올 수 없습니다")
        self.__height = height

    def get_area(self):
        return self.__width * self.__height

rect = Rect(10, 10) # 생성자를 통해서 변수 설정 가능, 음수를 넣으면 오류 출력
#print(rect.__width) # 오류, 외부에서 접근 불가능
rect.set_height(rect.get_height() + 10) # 현재의 높이에 10을 더한다.
print(rect.get_area()) # Exception: 너비와 높이는 음수가 나올 수 없습니다