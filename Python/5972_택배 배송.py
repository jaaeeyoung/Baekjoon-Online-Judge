'''
===================================================================================================================================
문제
===================================================================================================================================
[5972] 택배 배송
===================================================================================================================================
Log
===================================================================================================================================
' 2022-05-12 THU : 문제 파악
                   문제 해결
===================================================================================================================================
'''
'''
Algorithm
최단거리 - Dijkstra
1. 양방향 그래프 생성
2. Dijkstra 최단거리 구하기
'''

def dijkstra(start):
    queue = []
    # 시작 노드로 가는 최단 경로 0으로 설정
    heapq.heappush(queue, (start, 0))
    distance[start] = 0
    
    while queue:
        # 최단거리가 가장 짧은 노드 꺼내기
        now, dist = heapq.heappop(queue)
        
        # 이미 처리된 적 있는 노드인지 확인
        if distance[now] < dist:
            continue

        # 인접한 헛간으로 이동
        for i, C in graph[now]:
            cost = dist + C
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(queue, (i, cost))
    
import heapq
import sys
input = sys.stdin.readline
INF = 10e9

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
distance = [INF for _ in range(N+1)]
visited = [False for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

dijkstra(1)
print(distance[-1])