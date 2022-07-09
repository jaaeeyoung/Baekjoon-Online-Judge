'''
===================================================================================================================================
문제
===================================================================================================================================
[11403] 경로 찾기
===================================================================================================================================
Log
===================================================================================================================================
' 2022-07-09 SAT : 문제 파악
                   문제 해결
===================================================================================================================================
'''
'''
Algorithm
DFS
1. 그래프 구현
2. DFS 돌면서 갈 수 있는 곳 리스트에 저장
3. 리스트에 들어있는 곳에 맞게 1로 변경
'''

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(x):
    global idx
    # 현재 노드에 방문한 적 있는지 확인
    if visited[x]:
        return False
    
    # 방문 기록
    # dfs를 첫 번째 수행하는 경우가 아닐 때만 수행
    if x != idx or (nodes and x == idx):
        visited[x] = True
        nodes.append(x)
    
    # 인접 노드 방문
    for next_node in graph[x]:
        dfs(next_node)
    
    return True

def set_answer(i):
    for j in nodes:
        answer[i][j] = 1
        
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
answer = [[0 for _ in range(N)] for __ in range(N)]
# 그래프 구현
graph = [[] for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            graph[i].append(j)

# 모든 정점 DFS 돌기
for idx in range(N):
    nodes = []
    visited = [False for _ in range(N+1)]
    
    if dfs(idx):
        # set answer
        set_answer(idx)

for i in range(N):
    print(' '.join(map(str, answer[i])))