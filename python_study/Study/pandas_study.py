#데이터를 효과적으로 처리하고, 보여줄 수 있도록 도와주는 라이브러리
#인덱스에 따라 정보를 나열하므로 Dictionary에 가깝다.
#excel과 비슷
#series(데이터의 속성마다 해당하는 데이터를 모아놓은것, 모아서 데이터프레임이 된다) 를 기본자료형으로 사용

import pandas as pd
import numpy as np
#Series는 인덱스와 값으로 구성
array = pd.Series(['사과', '바나나','당근'], index = ['Apple', 'Banana', 'Carrot'])

print(array)
'''
a     사과
b    바나나
c     당근
dtype: object
'''
print(array['Apple']) # 사과

frequency_dict = {
    'Apple': 3,
    'Banana': 5,
    'Carrot': 7
}
frequency = pd.Series(frequency_dict) # dict와 같은구조여서 series로 만들 수 있다.
print(frequency['Apple']) # 3

#데이터프레임: 다수의 시리즈를 모아 처리하기 위한 목적, 표형태로 데이터를 출력
#이름(name) : 값(values)
summary = pd.DataFrame({ # 인덱스 기준으로 합침
    'word' : array,
    'frequency' : frequency
})
print(summary)
'''
       word  frequency
Apple    사과          3
Banana  바나나          5
Carrot   당근          7
'''

word = pd.Series(['사과','바나나','당근'], index = ['Apple','Banana','Carrot'])
frequency = pd.Series([3, 5, 7], index=['Apple','Banana','Carrot'])
importance = pd.Series([3, 2, 1], index=['Apple','Banana','Carrot'])
summary = pd.DataFrame({
    'word' : word,
    'frequency' : frequency,
    'importance' : importance
})
score = summary['frequency'] * summary['importance'] # 인덱스 기준으로 곱한다.
summary['score'] = score
print(summary)

#이름을 기준으로 슬라이싱
print(summary.loc['Banana':'carrot','importance':])
'''
        importance  score
Banana           2     10
Carrot           1      7
'''
#인덱스 기준으로 슬라이싱
print(summary.iloc[1:3,2:])
'''
        importance  score
Banana           2     10
Carrot           1      7
'''
summary.loc['Apple', 'importance'] = 5 # 데이터의 변경
summary.loc['Blueberry'] = ['블루베리',2,4,8] # 새 데이터 삽입
print(summary)
print()
summary.to_csv("C:/Users/LEEMINJUN/python_study/Study/pandas_summary.csv", encoding="utf-8-sig") # csv파일로 저장
saved = pd.read_csv("C:/Users/LEEMINJUN/python_study/Study/pandas_summary.csv", index_col=0) # 불러오기
print(saved)

print()
summary.loc['Banana','frequency'] = np.nan # not a number 데이터가 없다
print(summary)
print(summary.notnull())
print(summary.isnull())
summary['frequency'] = summary['frequency'].fillna('no data') # fillna('') 값이 nan인 데이터를 찾아서 문자를 넣어줌
# summary = summary.fillna('no data')  전체 nan에 대해 적용도 가능
print(summary)

print()
array1 = pd.Series([1, 2, 3], index=['A', 'B', 'C'])
array2 = pd.Series([4, 5, 6], index=['B', 'C', 'D'])

array = array1.add(array2, fill_value=0) # fill_value : 겹치지않는 인덱스의 데이터의 빈공간을 처리한다.
print(array)
'''
A    1.0
B    6.0
C    8.0
D    6.0
dtype: float64
'''
array_1 = array1.add(array2) # fill_value값을 정하지 않으면 겹치지 않는 데이터는 nan처리 한다
print(array_1)
'''
A    NaN
B    6.0
C    8.0
D    NaN
dtype: float64
'''

array1 = pd.DataFrame([[1, 2], [3, 4]], index=['A', 'B'])
array2 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=['B', 'C', 'D'])

print(array1)
print()
print(array2)

array = array1.add(array2, fill_value=0) # 겹치는데이터가 둘다 없으면 nan처리
print(array)
'''
     0    1    2
A  1.0  2.0  NaN
B  4.0  6.0  3.0
C  4.0  5.0  6.0
D  7.0  8.0  9.0
'''
print("컬럼 1의 합:", array[1].sum()) # 컬럼 1의 합: 21.0
print(array.sum()) # 각 칼럼에 대해서 합을 구해준다
'''
0    16.0
1    21.0
2    18.0
'''
print(summary)
summary = summary.sort_values('importance', ascending=False) # 정렬해줌(옵션으로 정렬할 열과 오름내림정함)
print(summary)
'''
           word frequency  importance  score
Apple        사과         3           5      9
Blueberry  블루베리         2           4      8
Banana      바나나   no data           2     10
Carrot       당근         7           1      7
'''

df = pd.DataFrame(np.random.randint(0,10,(2,2)), index=[0,1], columns=['A','B'])
print(df)
'''
   A  B
0  6  7
1  4  1
'''
print(df['A'] < 5)
'''
0    False
1     True
'''
print(df.query('A <= 5 and B <=8')) # query : 행단위로 조건이 맞는 데이터를 출력
'''
Name: A, dtype: bool
   A  B
1  4  1
'''
print()
df = pd.DataFrame([[1, 2, 3, 4], [1, 2, 3, 4]], index=[0, 1], columns=["A", "B", "C", "D"])
print(df)
'''
   A  B  C  D
0  1  2  3  4
1  1  2  3  4
'''
df = df.apply(lambda x: x + 1) # 함수를 먹일수도 있다. lambda도 가능
print(df)
'''
   A  B  C  D
0  2  3  4  5
1  2  3  4  5
'''
def addOne(x):
  return x + 1

df = df.apply(addOne) # 함수도 가능
print(df)

df = pd.DataFrame([
  ['Apple', 'Apple', 'Carrot', 'Banana'],
  ['Durian', 'Banana', 'Apple', 'Carrot']],
  index=[0, 1],
  columns=["A", "B", "C", "D"])

print(df)
df = df.replace({"Apple": "Airport"}) # 특정한 데이터를 찾아 값을 바꿈
print(df)
'''
         A        B        C       D
0  Airport  Airport   Carrot  Banana
1   Durian   Banana  Airport  Carrot
'''

print()
df = pd.DataFrame([
  ['Apple', 7, 'Fruit'],
  ['Banana', 3, 'Fruit'],
  ['Beef', 5, 'Meal'],
  ['Kimchi', 4, 'Meal']],
  columns=["Name", "Frequency", "Type"])

print(df)
print(df.groupby(['Type']).sum()) # 데이터의 그룹화, type을 기준으로 해당하는 종류들끼리 합쳤다
'''
       Frequency
Type
Fruit         10    #7+3
Meal           9    #5+4
'''
df = pd.DataFrame([
  ['Apple', 7, 5, 'Fruit'],
  ['Banana', 3, 6, 'Fruit'],
  ['Beef', 5, 2, 'Meal'],
  ['Kimchi', 4, 8, 'Meal']],
  columns=["Name", "Frequency", "Importance", "Type"])

print(df)
print(df.groupby(["Type"]).aggregate([min, max, np.average])) #여러개의 groupby연산을 한번에 수행할 수있다.
'''
      Frequency             Importance
            min max average        min max average
Type
Fruit         3   7     5.0          5   6     5.5
Meal          4   5     4.5          2   8     5.0
'''

def my_filter(data): # filter에 먹일 함수는 해당데이터의 형식에 맞아야한다.
  return data["Frequency"].mean() >= 5

print(df)
# 스스로 함수를 만들어 groupby를 실행할수있다.
print(df.groupby("Type").filter(my_filter))

#Type에서 Fruit의 값을 같는행을 출력
print(df.groupby("Type").get_group("Fruit"))

#Gap 열을 추가하고 값들은 Frequency에서 평균값을 뺀것으로 한다.
#그룹별로 각각의 셀에 대해서 연산을 수행한다.
df["Gap"] = df.groupby("Type")["Frequency"].apply(lambda x: x - x.mean())
print(df)
'''
     Name  Frequency  Importance   Type  Gap
0   Apple          7           5  Fruit  2.0
1  Banana          3           6  Fruit -2.0
2    Beef          5           2   Meal  0.5
3  Kimchi          4           8   Meal -0.5
'''

#데이터 프레임의 다중화
df = pd.DataFrame(
  np.random.randint(1, 10, (4, 4)),
  index=[['1차', '1차', '2차', '2차'], ['공격', '수비', '공격', '수비']],
  columns=['1회', '2회', '3회', '4회']
)
#index를 2차원리스트형태로 설정하면, 같은값을 갖는 인덱스는 묶어서 나타낸다.
print(df)
'''
       1회  2회  3회  4회
1차 공격   5   8   6   3
   수비   1   9   8   3
2차 공격   4   7   5   1
   수비   4   1   5   5
'''
print(df[["1회", "2회"]].loc["2차"])

df = pd.DataFrame([
    ['Apple', 7, 5, 'Fruit'],
    ['Banana', 3, 6, 'Fruit'],
    ['Coconut', 2, 6, 'Fruit'],
    ['Rice', 8, 2, 'Meal'],
    ['Beef', 5, 2, 'Meal'],
    ['Kimchi', 4, 8, 'Meal']],
    columns=["Name", "Frequency", "Importance", "Type"])

#print(df)
df = df.pivot_table(
    index="Importance", columns="Type", values="Frequency",
    aggfunc=np.max
)
print(df)
'''
Type        Fruit  Meal
Importance
2             NaN   8.0
5             7.0   NaN
6             3.0   NaN
8             NaN   4.0
'''