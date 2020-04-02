#바이너리 파일 : 010100010(이미지, 동영상, 워드, 엑셀, PDF)
#텍스트 파일 : 운영체제가 내부적으로 데이터를 쉽게 다룰수있게해주는파일, 텍스트에디터로 열수있음
# - 쓰기(write) w
# - 있는 파일 뒤에쓰기(append) a
# - 읽기(read) r

file = open("file_test.txt", "w", encoding="utf8")# a로 하면 뒤에 추가한다.("file_test.txt", "w", encoding = "utf8")
#로해야 file_test.txt.에서 깨지지않고 볼수있다.
file.write("파일 테스트, ")
file.close()

'''
with open("file_test.txt", "w", encoding="utf8") as file:
    file.write("~~~~")
    ''' #위와 같은코드 with로 파일을 열면 close도 같이 해준다.

file = open("file_test.txt", "r", encoding="utf8")
print(file.read())
file.close()