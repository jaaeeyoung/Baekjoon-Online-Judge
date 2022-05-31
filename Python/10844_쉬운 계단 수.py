'''
===================================================================================================================================
문제
===================================================================================================================================
[10844] 쉬운 계단 수
===================================================================================================================================
Log
===================================================================================================================================
' 2022-04-20 WED : 문제 파악
                   틀림
                   점화식 다시 세워봐야될듯
' 2022-05-12 THU : 점화식 다시 생각해보기
' 2022-05-31 TUE : 시간 초과
                   질문에 나와있는 해설 참고
                   문제 해결
===================================================================================================================================
'''
'''
Algorithm
Dynamic Programming
i : 숫자 자릿수, j : j로 시작하는 숫자의 개수
dp[i][j] = dp[i-1][1] (j == 0)
dp[i][j] = dp[i-1][8] (j == 9)
dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1] (j != 0, j != 9)
'''

N = int(input())
dp = [[0 for _ in range(10)] for _ in range(N+1)]
dp[1] = [1 for _ in range(10)]

for i in range(2, N+1):
    for j in range(10):
        # j가 0이면 1로 변경
        if j == 0:
            dp[i][j] = dp[i-1][1]
        # j가 9이면 i-1의 j-1의 값과 동일
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        # 그 외의 경우
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print((sum(dp[N])-dp[N][0])%1000000000)