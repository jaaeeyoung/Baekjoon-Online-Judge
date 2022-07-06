'''
===================================================================================================================================
문제
===================================================================================================================================
[2583] 영역 구하기
===================================================================================================================================
Log
===================================================================================================================================
' 2022-07-06 WED : 문제 파악
                   문제 해결
===================================================================================================================================
'''
'''
Algorithm
DFS
1. 입력받은 꼭지점을 기준으로 사각형의 값 1로 채움
2. DFS를 통해 0인 공간의 개수와 넓이 구하기
'''

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y):
    global count

    # graph 밖으로 벗어나거나 1이면 False 반환
    if x < 0 or y > M-1 or y < 0 or x > N-1:
        return False
    
    # 이미 방문한 곳이면 False 반환
    if visited[x][y] or graph[x][y] == 1:
        return False
    
    # 방문 기록
    visited[x][y] = True
    # 칸 수 세기
    count += 1
    
    # 인접 노드로 이동
    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)
    
    return True

M, N, K = map(int, input().split())
inputs = [list(map(int, input().split())) for _ in range(K)]

# 입력받은 좌표를 기준으로 사격형의 값을 1로 채움
graph = [[0 for yy in range(M)] for xx in range(N)]
visited = [[False for yy in range(M)] for xx in range(N)]
for x1, y1, x2, y2 in inputs:
    for x in range(x1, x2):
        for y in range(y1, y2):
            graph[x][y] = 1

# DFS 이용해 0인 공간의 개수와 넓이 구하기
answer = [0]
for x in range(N):
    for y in range(M):
        count = 0
        if dfs(x, y):
            answer[0] += 1
            if count != 0:
                answer.append(count)

print(answer[0])
answer = answer[1:]
answer.sort()
print(' '.join(map(str, answer)))