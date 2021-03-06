'''
===================================================================================================================================
문제
===================================================================================================================================
[11050] 이항 계수 1
===================================================================================================================================
Log
===================================================================================================================================
' 2022-03-05-SAT : 문제 파악
                   문제 해결
===================================================================================================================================
'''

'''
1. N * ... * 1을 총 K번 진행
2. K! 계산
3. 1번의 결과를 2번의 결과로 나눔
'''

# Factorial 계산하는 함수
def factorial(K):
    if K < 2:
        return 1
    else:
        return K * factorial(K-1)
    
# 입력
N, K = map(int, input().split())

# N * N-1 * ...
num1 = 1
for i in range(K):
    num1 *= N-i

# K!
num2 = factorial(K)

# N * N-1 * ... // K!
print(num1 // num2)