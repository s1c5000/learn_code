'''
디지털 시계에 하루동안(00:00~23:59) 3이 표시되는 시간을 초로 환산하면 총 몇 초(second) 일까요?
디지털 시계는 하루동안 다음과 같이 시:분(00:00~23:59)으로 표시됩니다.
00:00 (60초간 표시됨)
00:01 
00:02 
...
23:59
'''
hours = [str(i) for i in range(0,24)]
minutes = [str(i) for i in range(0,60)]
count = 0
for i in hours:
    if '3' in i:
        count = count + 3600
    else:
        for j in minutes:
            if '3' in j:
                count = count + 60 
print(count)