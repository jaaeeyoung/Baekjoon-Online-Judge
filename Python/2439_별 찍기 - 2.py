'''
===================================================================================================================================
문제
===================================================================================================================================
[2439] 별 찍기 - 2
===================================================================================================================================
Log
===================================================================================================================================
' 2022-05-29 SUN : 문제 파악
                   문제 해결
===================================================================================================================================
'''
'''
Algorithm
구현
'''

N = int(input())
for i in range(1, N+1):
    print(' '*(N-i) + '*'*i)