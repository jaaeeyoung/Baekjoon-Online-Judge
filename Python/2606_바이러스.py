'''
===================================================================================================================================
문제
===================================================================================================================================
[2606] 바이러스
===================================================================================================================================
시간 및 메모리 제한
===================================================================================================================================
# 시간 제한 : 1 초
# 메모리 제한 : 128 MB
===================================================================================================================================
문제 설명
===================================================================================================================================
# 신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든
  컴퓨터는 웜 바이러스에 걸리게 된다.

# 예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자. 1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 
  컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다. 하지만 4번과 7번 컴퓨터는 1번 컴퓨터 
  와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.

# 어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이
  러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.
===================================================================================================================================
입력
===================================================================================================================================
# 첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다. 둘째 줄에는 네트워크 상
  에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍
  이 주어진다.
===================================================================================================================================
출력
===================================================================================================================================
# 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.
===================================================================================================================================
입출력 예
===================================================================================================================================
입력 1
7
6
1 2
2 3
1 5
5 2
5 6
4 7

출력 1
4
===================================================================================================================================
알고리즘 분류
===================================================================================================================================
# 그래프 이론
# 그래프 탐색
# 너비 우선 탐색
# 깊이 우선 탐색
===================================================================================================================================
Log
===================================================================================================================================
' 2022-02-22-TUE : 문제 파악
                   틀렸습니다. -> 맞는 것 같은데 어디서 틀린건지 모르겠음
' 2022-02-23-WED : BFS로 구현해도 틀림
                   컴퓨터간의 연결을 리스트에 저장할 때 단방향으로만 적어서 틀린거였음
                   -> 양방향으로 고쳐 맞음
                   문제 해결
===================================================================================================================================
'''

N = int(input()) # 컴퓨터 수
M = int(input()) # 네트워크 상에서 직접 연결되어있는 컴퓨터 쌍의 수

graph = []
visited = [False] * (N+1)
for i in range(N+1):
    graph.append([])
    
for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    if i not in graph[j]:
          graph[j].append(i)

def dfs(n):
    # 현재 컴퓨터 방문 처리
    visited[n] = True
    # 연결되어있는 컴퓨터 하나씩 방문
    for i in graph[n]:
        if not visited[i]:
            dfs(i)

# dfs(1)

# count = -1
# for i in visited: # 방문한 노드 수 세기
#     if i:
#         count += 1
# print(count)

# BFS
from collections import deque

def bfs(start):
      queue = deque([start])
      
      
      while queue:
            now = queue.popleft()
            # 현재 컴퓨터 방문 처리
            visited[now] = True
            # print('now:', now)
            # print('visited:', visited)
            
            # 해당 노드의 인접 노드 중 방문하지 않은 노드를 모두 Queue에 삽입하고 방문처리
            for i in graph[now]:
                  if not visited[i]:
                        queue.append(i)

bfs(1)

count = -1
for i in visited: # 방문한 노드 수 세기
    if i:
        count += 1
print(count)