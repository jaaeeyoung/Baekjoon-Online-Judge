'''
===================================================================================================================================
문제
===================================================================================================================================
[2441] 별 찍기 - 4
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
for i in range(N):
    print(' '*i + '*'*(N-i))