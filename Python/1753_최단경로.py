'''
===================================================================================================================================
문제
===================================================================================================================================
[1753] 최단경로
===================================================================================================================================
Log
===================================================================================================================================
' 2022-03-20-SUN : 문제 파악
                   문제 해결
===================================================================================================================================
'''
'''
Algorithm
dijkstra 알고리즘 - 힙 
1. 입력으로 graph 구성
2. 다익스트라 알고리즘을 이용해 최단 경로 구하기
'''

import sys
import heapq

def dijkstra(start):
    queue = []
    # 첫 번째 노드 큐에 추가
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    
    while queue:
        # 큐에서 꺼내기
        dist, now = heapq.heappop(queue)
        
        # 이미 방문한 노드는 무시
        if distance[now] < dist:
            continue
        
        # 인접 노드 확인
        for next in graph[now]:
            # cost 계산 = 현재 node의 거리 + 다음 node까지의 거리
            cost = dist + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                # 큐에 추가
                heapq.heappush(queue, (cost, next[0]))

INF = int(1e9)
input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dijkstra(start)
for i in range(1, V+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])