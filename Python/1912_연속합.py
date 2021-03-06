'''
===================================================================================================================================
문제
===================================================================================================================================
[1912] 연속합
===================================================================================================================================
Log
===================================================================================================================================
' 2022-06-01-WED : 문제 파악
                   4% 시간 초과
                   37% 틀렸습니다
===================================================================================================================================
'''
'''
Algorithm
Dynamic Programming
dp[i] = max(1~i까지 누적합, 앞에서부터 하나씩 누락하면서 누적합, 직전 값 + 현재 값)
'''

import sys
input = sys.stdin.readline
n = int(input())
arr = [int(num) for num in input().split()]

dp = [0] * n
dp[0] = arr[0]
if n > 1:
    dp[1] = max(sum(arr[:2]), arr[1])

for i in range(2, n):
    if dp[i-1] < 0:
        dp[i] = max(arr[i], dp[i-1] + arr[i])
    else:
        dp[i] = dp[i-1] + arr[i]

print(max(dp))