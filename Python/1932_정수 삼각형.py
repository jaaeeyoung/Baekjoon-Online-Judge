'''
===================================================================================================================================
문제
===================================================================================================================================
[1932] 정수 삼각형
===================================================================================================================================
Log
===================================================================================================================================
' 2022-05-09 MON : 문제 파악
                   문제 해결
===================================================================================================================================
'''
'''
Algorithm
Dynamic Programming
dp[i+1][j] = max(dp[i+1][j], dp[i][j] + table[i+1][j])
dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + table[i+1][j+1])
'''

N = int(input())
table = [[] for _ in range(N+1)]
for i in range(1, N+1):
    table[i] += list(map(int, input().split()))
    
dp = [[] for _ in range(N+1)]
for i in range(N+1):
    for j in range(i):
        dp[i].append(0)

dp[1] = table[1]
for i in range(1, len(table)-1):
    for j in range(len(table[i])):
        dp[i+1][j] = max(dp[i+1][j], dp[i][j] + table[i+1][j])
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + table[i+1][j+1])

print(max(dp[-1]))