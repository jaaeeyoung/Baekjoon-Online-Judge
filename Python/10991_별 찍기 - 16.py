'''
===================================================================================================================================
문제
===================================================================================================================================
[10991] 별 찍기 - 16
===================================================================================================================================
Log
===================================================================================================================================
' 2022-05-30 MON : 문제 파악
                   문제 해결
===================================================================================================================================
'''
'''
Algorithm
구현
'''

def func(num):
    answer = ''
    for _ in range(num-1):
        answer += '* '
    return answer + '*'

N = int(input())
if N > 1:
    for i in range(1, N+1):
        print(' '*(N-i) + func(i))
else:
    print('*')