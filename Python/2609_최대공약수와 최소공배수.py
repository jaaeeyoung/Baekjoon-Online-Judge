'''
===================================================================================================================================
문제
===================================================================================================================================
[2609] 최대공약수와 최소공배수
===================================================================================================================================
Log
===================================================================================================================================
' 2022-03-05-SAT : 문제 파악
                   문제 해결
===================================================================================================================================
'''

'''
1. 유클리드 호제법 이용
    1.1. 유클리드 호제법 함수 생성 - 재귀
    1.2. A와 B의 최대 공약수는 B와 A%B의 최대공약수와 같다.
2. 최소공배수 = A*B%최대공약수
'''

import sys
input = sys.stdin.readline

def euclid(A, B):
    R = A % B
    # A가 B의 배수이면 Return
    if R == 0:
        return B
    return euclid(B, R)

A, B = map(int, input().split())
answer = euclid(max(A, B), min(A, B))
print(answer)
print(A * B // answer)