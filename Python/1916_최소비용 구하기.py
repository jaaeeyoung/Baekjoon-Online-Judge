'''
===================================================================================================================================
문제
===================================================================================================================================
[1916] 최소비용 구하기
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
    
    # 첫 번째 위치 큐에 추가
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    
    while queue:
        # queue에서 꺼내기
        dist, now = heapq.heappop(queue)
        
        # 이미 방문한 적 있는 도시이면 무시
        if distance[now] < dist:
            continue
        
        # 인접 노드 확인
        for next in graph[now]:
            # cost 계산 : 현재 node의 누적 거리 + 현재 노드에서 다음 노드까지의 거리
            cost = dist + next[0]
            # cost가 distance에 저장된 값보다 작으면 갱신
            if cost < distance[next[1]]:
                distance[next[1]] = cost
                heapq.heappush(queue, (cost, next[1]))
                
input = sys.stdin.readline
INF = 1e9

# 입력
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)
for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((cost, end))
start, end = map(int, input().split())

dijkstra(start)
print(distance[end])