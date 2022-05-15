'''
===================================================================================================================================
문제
===================================================================================================================================
[13023] ABCDE
===================================================================================================================================
Log
===================================================================================================================================
' 2022-05-12 THU : 문제 파악
                   정점이 몇개이던간에 5개의 연속 EDGE가 있으면 된다. -> 알고리즘 다시 생각
===================================================================================================================================
'''
'''
Algorithm
BFS
1. 양방향 그래프 구현
2. BFS 수행해 덩어리가 1개이면 조건에 맞는 경우 (1 출력)
   덩어리가 2개 이상이면 조건에 맞지 않는 경우 (0 출력)
'''

def BFS(start):

    queue = deque([start])
    
    # 방문한 적 있는지 확인
    if visited[start]:
        return False
    
    # 방문 기록
    visited[start] = True
    print(start)
    while queue:
        # print(queue)
        now = queue.popleft()
        # print('now:', now)
        # print('graph:', graph[now])
        # 주변 노드 없으면 return
        if not graph[now] and now < N-1:
            # print('no')
            # continue
            return False
        
        # 주변 노드 모두 방문
        for next_node in graph[now]:
            
            # 방문한 적 있으면 continue
            if visited[next_node]:
                continue
            
            # 방문 기록
            visited[next_node] = True
            print(next_node)
            
            # queue에 모두 추가
            queue.append(next_node)
        # return True

def DFS(start):
    global count
    print()
    print('start:', start)
    
    # 이미 방문한 적 있는지 확인
    if visited[start]:
        # print('here1')
        return False
    # print('here2')
    # 방문 기록
    visited[start] = True
    
    # 인접 노드가 없으면 return
    if not graph[start]:
        print('hi')
        return False
    
    # 인접 노드 방문
    for next_node in graph[start]:
        print('next_node:', next_node)
        count += 1
        print('count:', count)
        if not DFS(next_node):
            return
        
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
visited = [False for _ in range(N)]
for _ in range(M):
    first, second = map(int, input().split())
    graph[first].append(second)
    # graph[second].append(first)

count = 0 # 노드 덩어리 개수
for i in range(N):
    # print()
    # print('i:', i)
    count = 0 # 노드 덩어리 개수
    visited = [False for _ in range(N)]
    DFS(i)
    if count > 3:
        break
print()
# 덩어리가 1개이면 1 출력
if count > 3:
    print(1)
else:
    print(0)