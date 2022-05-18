'''
===================================================================================================================================
문제
===================================================================================================================================
[13913] 숨바꼭질 4
===================================================================================================================================
Log
===================================================================================================================================
' 2022-05-16 MON : 문제 파악
                   순서를 어떻게 출력해야할지 모르겠음
===================================================================================================================================
'''
'''
Algorithm
DP
1. DP Table에 현재까지 가장 짧은 시간 저장
   -> dp[x], dp[x//2], dp[x-1], dp[x+1] 비교 필요
'''
INF = 2000001

def BFS(start):
    directions = [-1, 1]
    queue = deque([start])
    
    # 방문한 적 있으면 RETURN
    if graph[start] > 0:
        return False
    graph[start] = 1
    
    while queue:
        now = queue.popleft()
        print('now:', now)
        
        # 앞뒤로 이동
        for dir in directions:
            next_node = now + dir
            
            # 방문한 적 있으면 continue
            if graph[next_node] > 0:
                continue
            
            graph[next_node] = graph[now] + 1
            
            # queue에 추가
            queue.append(next_node)
        
        # 순간 이동
        next_node = now * 2
        # 방문한 적 있으면 continue
        if graph[next_node] > 0:
            continue
        graph[next_node] = graph[now]+1
        # queue에 추가
        queue.append(next_node)
        
        if now == K:
            break
    
from collections import deque
N, K = map(int, input().split())
graph = [0 for _ in range(INF)]
BFS(N)
print(graph[:18])

# 
# dp = [INF for _ in range(INF)]
# dp[N] = 0
# for x in range(N+1, K*2):
#     dp[x] = min(dp[x], min(dp[x//2], dp[x-1]))+1

# for x in range(N+1, K*2):
#     if dp[x] > dp[x+1]:
#         dp[x] = dp[x+1]+1
# print(dp[N:19])