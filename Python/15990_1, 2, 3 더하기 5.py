'''
===================================================================================================================================
문제
===================================================================================================================================
[15990] 1, 2, 3 더하기 5
===================================================================================================================================
Log
===================================================================================================================================
' 2022-04-13 WED : 문제 파악
                   알고리즘 다시 짜야될듯
===================================================================================================================================
'''
'''
Algorithm
Dynamic Programming
dp[i] = dp[j]+dp[i-j]
'''

# T = int(input())
n = int(input())

dp = [0] * (n+1)
dp[1] = 1
if n > 1:
    dp[2] = 1
if n > 2:
    dp[3] = 3
    
for i in range(4, n+1):
    for j in range(1, n//2+1):
        dp[i] = max(dp[j]*dp[i-j], dp[i])
print(dp[-1])