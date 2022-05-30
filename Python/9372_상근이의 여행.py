'''
===================================================================================================================================
문제
===================================================================================================================================
[9372] 상근이의 여행
===================================================================================================================================
Log
===================================================================================================================================
' 2022-05-30-MON : 문제 파악
                   dfs - 50%에서 시간 초과
                   방문하지 않은 국가만 dfs 돌도록 구현
                   input을 sys.stdin.readline으로 설정
                   문제 해결
===================================================================================================================================
'''

'''
DFS
1. 그래프 구현 (단방향)
2. DFS 돌면서 몇 개의 간선이 있는지 확인
'''

import sys
input = sys.stdin.readline

def dfs(country):
    global answer # 간선 개수
    
    # 방문한 기록 있으면 return
    if visited[country]:
        return
    
    # 방문 기록
    visited[country] = True
    answer += 1
    
    # 인접 국가 여행
    for next_country in graph[country]:
        dfs(next_country)

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    answer = -1
    visited = [False for _ in range(N+1)]
    
    # graph 구현
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)

    # dfs 돌면서 간선 개수 확인
    for country in range(1, N+1):
        # 방문하지 않은 국가만 확인
        if not visited[country]:
            dfs(country)
    
    print(answer)