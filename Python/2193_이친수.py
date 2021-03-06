'''
===================================================================================================================================
문제
===================================================================================================================================
[2193] 이친수
===================================================================================================================================
Log
===================================================================================================================================
' 2022-05-31 TUE : 문제 파악
                   문제 해결
===================================================================================================================================
'''
'''
Algorithm
Dynamic Programming
점화식 : dp[i] = dp[i-1] + dp[i-2]
'''

N = int(input())
dp = [0] * (N+1)
dp[1] = 1
if N > 1:
    dp[2] = 1
    
for idx in range(2, N+1):
    dp[idx] = dp[idx-1] + dp[idx-2]

print(dp[N])