'''
===================================================================================================================================
문제
===================================================================================================================================
[1446] 지름길
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
1. 지름길을 입력 받아 graph 생성 
    ➝ 도착 지점이 고속도로의 길이보다 큰 경우 graph에 추가하지 않음 
2. 지름길이 아닌 길도 graph에 추가 
    ➝ 중간에 끊겨있는 길도 같이 추가
3. D 위치의 최단 거리 출력
'''
import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline

def dijkstra(start):
    queue = []
    
    # 첫 번째 칸으로 가는 최단 경로 0으로 설정
    heapq.heappush(queue, (start, 0))
    distance[start] = 0
    
    while queue:
        
        # 큐에서 꺼내기
        dist, now = heapq.heappop(queue)
        
        # 방문한 노드라면 무시
        if distance[now] < dist:
            continue
        
        # 인접 노드 확인
        for next in graph[now]:
            cost = dist + next[1]
            
            # cost가 인접노드까지 가는 데 최소 거리라면 갱신하고 큐에 추가
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(queue, (cost, next[0]))
    

N, D = map(int, input().split())
graph = [[] for _ in range(D+1)]
distance = [INF] * (D+1)
for _ in range(N):
    start, end, length = map(int, input().split())
    # 도착 지점이 고속도로의 길이보다 큰 경우 graph에 추가하지 않음
    if end > D:
        continue
    graph[start].append((end, length))

    # 지름길이 아닌 길도 graph에 추가
    if (end, end - start) not in graph[start]:
        graph[start].append((end, end - start))
        
for i in range(D):
    # graph의 현재 INDEX에 다음 칸 까지의 거리 추가
    graph[i].append((i+1, 1))

dijkstra(0)
print(distance[-1])