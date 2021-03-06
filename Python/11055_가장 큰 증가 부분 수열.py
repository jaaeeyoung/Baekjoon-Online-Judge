'''
===================================================================================================================================
문제
===================================================================================================================================
[11055] 가장 큰 증가 부분 수열
===================================================================================================================================
Log
===================================================================================================================================
' 2022-06-01-WED : 문제 파악
                   문제 해결
===================================================================================================================================
'''
'''
Algorithm
Dynamic Programming
점화식 : dp[i] = max(dp[i], dp[j]+A[i])
'''

N = int(input())
A = [int(num) for num in input().split()]

dp = A[:]
dp[0] = A[0]
for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + A[i])

print(max(dp))