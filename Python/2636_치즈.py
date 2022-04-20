'''
===================================================================================================================================
문제
===================================================================================================================================
[2636] 치즈
===================================================================================================================================
Log
===================================================================================================================================
' 2022-04-15 FRI : 문제 파악
                   런타임 에러(Recursion Error)
' 2022-04-16 SAT : 문제 해결
                   코드가 너무 지저분해 최적화해보기
' 2022-04-20 WED : 코드 최적화
===================================================================================================================================
'''
'''
Algorithm
DFS - 재귀
1. 1시간마다 DFS를 이용해 치즈에 구멍이 있는지 확인
    -> 0으로된 덩어리가 2개 이상인 경우 구멍 존재
2. 구멍이 존재하면 구멍에 해당하는 칸의 값을 H로 변경
3. graph를 한 번씩 돌면서 현재 위치가 1인데 상, 하, 좌, 우 중 한 칸이라도 0이 존재하면 이번에 삭제되는 칸
    -> 해당 칸의 값을 C로 변경
4. 매 번 C의 개수 갱신해 출력
'''

def dfs(x, y, replace_value):
    
    # graph 밖으로 벗어나면 False Return
    if x < 0 or x > N-1 or y < 0 or y > M-1:
        return False
    
    # 이미 방문했던 칸이거나 0이 아니면 False Return
    if visited[x][y] or graph[x][y] != 0:
        return False
    
    # 현재 위치 방문 기록
    visited[x][y] = True
    # 구멍인 경우 H로 변경
    graph[x][y] = replace_value
    
    # 상하좌우로 이동
    dfs(x-1, y, replace_value)
    dfs(x+1, y, replace_value)
    dfs(x, y-1, replace_value)
    dfs(x, y+1, replace_value)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
sys.setrecursionlimit(N*M)
graph = []
count_cheezes = 0 # 치즈가 녹기 전 치즈조각이 놓여 있는 칸의 개수
for _ in range(N):
    graph.append(list(map(int, input().split())))
    count_cheezes += graph[-1].count(1)

num = 0
while True:

    # 구멍의 값을 H로 변경
    visited = [[False for _ in range(M)] for _ in range(N)]
    for x in range(N):
        for y in range(M):
            # x, y가 0, 0이 아니면 replace 값 H로 설정
            if x > 0 and y > 0:
                dfs(x, y, 'H')
            else:
                dfs(x, y, 0)

    # 가장자리에 있는 1을 C로 변경
    count_c = 0
    for x in range(N):
        for y in range(M):
            if graph[x][y] == 1:
                # 현재 index의 상하좌우 중 한 군데라도 0이 있으면 가장자리
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx = x+dx
                    ny = y+dy
                    # graph 밖으로 벗어나면 continue
                    if nx < 0 or nx > N-1 or ny < 0 or ny > M-1:
                        continue
                    
                    # nx, ny가 0이면 x, y를 C로 변경하고 break
                    if graph[nx][ny] == 0:
                        graph[x][y] = 'C'
                        count_c += 1
                        break
    
    # 현재 1인 칸과 없어질 칸의 차가 0이면 break
    if count_cheezes - count_c == 0:
        print(num+1)
        print(count_cheezes)
        break
    
    # C, H인 칸 모두 0으로 변경
    for x in range(N):
        for y in range(M):
            if graph[x][y] == 'C'or graph[x][y] == 'H':
                graph[x][y] = 0
    num += 1
    count_cheezes -= count_c