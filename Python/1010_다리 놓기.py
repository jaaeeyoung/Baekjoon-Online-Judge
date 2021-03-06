'''
===================================================================================================================================
문제
===================================================================================================================================
[1010] 다리 놓기
===================================================================================================================================
Log
===================================================================================================================================
' 2022-03-06-SUN : 문제 파악
                   문제 해결
===================================================================================================================================
'''

'''
1. nCk 조합 계산 :  n! // (k! * (n-k)!)
    -> M 개 중에 N개를 골라서 다리를 놔야하기 때문
'''

def factorial(num):
    if num < 2:
        return 1
    else:
        return num * factorial(num-1)

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(factorial(M) // (factorial(N) * factorial(M - N)))