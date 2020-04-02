#dict는 중괄호로 묶으면된다 "키" : "값"
human = {
    "name": "Lee",
    "age": 222,
    "fav_food": ["kimchi", "icecream"]#리스트도 추가가능하지만 키로는 사용할수 없다. dictionary도 추가가능
}
 #print(human[0])리스트처럼 순서로 접근하려하면 오류가 난다
print(human["name"]) #Lee dict는 키로 값 접근한다.
human["hight"] = 200 #딕셔너리["key"] = 값으로 키와 값 추가가능
human["name"] = "kim" # 키로 접근해서 값 변경가능
del human["age"] #키로 접근해서 삭제가능 del
print(human)
print(type(human)) # dict

딕셔너리 = {
    "키" : "값",
    "문자" : "문자열",
    "리스트" : "[]"
}
for k in 딕셔너리: #k변수에는 딕셔너리의 key가 들어간다
    print("{} : {}".format(k, 딕셔너리[k]))

if "나이" in 딕셔너리: # 키가 있는지 확인을 할 수있다.
    print(딕셔너리["나이"])
else:
    print("해당키가 없습니다")

if 딕셔너리["키"] in 딕셔너리: # 해당키 없다고 나옴, 값으로는 접근불가능
    print(딕셔너리["나이"])
else:
    print("해당키가 없습니다2")

pets = [ #리스트도 안에 딕셔너리 요소로 가질수있다.
    {"name" : "뽀삐", "age" : 3},
    {"name" : "초코", "age" : 4},
    {"name" : "푸룽", "age" : 9},
    {"name" : "휴지", "age" : 2},
]
for pet in pets:# pet에 하나의 딕셔너리가 들어간다
    print("{}의 나이는{}".format(pet["name"], pet["age"]))  #뽀삐의 나이는3, 초코의 나이는4...

character = {
    "name" : "기사",
    "level" : 12,
    "item" : {
        "sword" : "불꽃의 검",
        "armor" : "풀플레이트"
    },
    "skill" : ["베기", "세게 베기" , "아주세게베기"]
}
for key in character: # key에 들어가는 값 : name, level, item, skill
    if type(character[key]) is dict: # character[item]일때 dict이므로 실행
        for k in character[key]: # k에 들어가는 값 :  "sword", "armor" /character[key] = "sword" : "불꽃의 검", "armor" : "풀플레이트"
            print("{} : {} ".format(k, character[key][k])) #  character[item][sword] =  불꽃의 검
    elif type(character[key]) is list: # character[skill]일때 list이므로 실행
        for s in character[key]: # s에 들어가는 값 :  "베기", "세게 베기" , "아주세게베기"
            print("{} : {}".format(key, s))
    else:
        print("{} : {}".format(key, character[key]))

#items() key와 value 값을 나눠서 각 변수에 넣어준다
a = {"key_1" : "value_1", "key_2" : "value_2", "key_3" : "value_3"}
for key, value in a.items(): # list의 enumerate()함수와 비슷
    print("{}키의 값은{}".format(key,value))# key_1키의 값은value_1, key_2키의 값은value_2
    print("{key}키의 값은{value}".format(key=key,value=value)) 