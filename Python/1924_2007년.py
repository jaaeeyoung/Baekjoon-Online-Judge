'''
===================================================================================================================================
문제
===================================================================================================================================
[1924] 2007년
===================================================================================================================================
Log
===================================================================================================================================
' 2022-05-23 MON : 문제 파악
                   문제 해결
===================================================================================================================================
'''
'''
Algorithm
입출력
'''

x, y = map(int, input().split())
yoil = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

# 월 계산
day = 0
for i in range(1, x):
    if i in [1, 3, 5, 7, 8, 10, 12]:
        day = (day + 31) % 7
    elif i in [4, 6, 9, 11]:
        day = (day + 30) % 7
    else:
        day = (day + 28) % 7

# 일 계산
day = (day + y) % 7
print(yoil[day])