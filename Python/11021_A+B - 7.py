'''
===================================================================================================================================
문제
===================================================================================================================================
[11021] A+B - 7
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

T = int(input())
for i in range(1, T+1):
    print('Case #{}:'.format(i), sum(map(int, input().split())))