'''
===================================================================================================================================
문제
===================================================================================================================================
[1987] 알파벳
===================================================================================================================================
Log
===================================================================================================================================
' 2022-03-31-THU : 문제 파악
                   
===================================================================================================================================
'''
'''
Algorithm
DFS
1. graph에 알파벳 저장
2. dfs를 이용해 탐색하면서 각 칸까지 몇 번 이동해 도착하는지 리스트에 저장
3. 리스트에서 가장 큰 값 출력
'''

import sys
input = sys.stdin.readline

R, C = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(list(input().rstrip()))

# 방향: 상, 하, 좌, 우
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
list_ = [graph[0][0]]
x, y = 0, 0
# while True:
#     # 상하좌우로 이동
#     for dx, dy in directions:
#         nx = x + dx
#         ny = y + dy
        
#         # 범위 밖으로 나가면 continue
#         if nx < 0 or nx > R-1 or ny < 0 or ny > C-1:
#             continue
        

# N, M = map(int, input().split())
# graph = []
# for _ in range(N):
#   graph.append(list(map(int, input())))
visited = [[False for _ in range(C)] for _ in range(R)]

def dfs(x, y):
  if x < 0 or x > R-1 or y < 0 or y > C-1 or visited[x][y]:
    return False

  # 현재 위치 방문 처리
  visited[x][y] = True
  print(graph[x][y])

  # 현재 노드와 인접한 노드 모두 찾기 (상, 하, 좌, 우 확인)
  dfs(x-1, y)
  dfs(x+1, y)
  dfs(x, y-1)
  dfs(x, y+1)

  return True

count = 0
for x in range(R):
  for y in range(C):
    if dfs(x, y) == True:
        print()
        count += 1

print(count)