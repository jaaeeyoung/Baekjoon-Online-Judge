'''
===================================================================================================================================
문제
===================================================================================================================================
[11724] 연결 요소의 개수
===================================================================================================================================
시간 및 메모리 제한
===================================================================================================================================
# 시간 제한 : 3 초
# 메모리 제한 : 512 MB
===================================================================================================================================
문제 설명
===================================================================================================================================
# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
===================================================================================================================================
입력
===================================================================================================================================
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 
  주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.
===================================================================================================================================
출력
===================================================================================================================================
# 첫째 줄에 연결 요소의 개수를 출력한다.
===================================================================================================================================
입출력 예
===================================================================================================================================
입력 1
6 5
1 2
2 5
5 1
3 4
4 6

출력 1
2

입력 2
6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3

출력 2
1
===================================================================================================================================
알고리즘 분류
===================================================================================================================================
# 수학
# 정수론
# 소수 판정
===================================================================================================================================
Log
===================================================================================================================================
' 2022-03-01-TUE : 문제 파악
                   문제 해결
===================================================================================================================================
'''
import sys
input = sys.stdin.readline


def dfs(start):

    # 현재 Node가 이미 방문한 Node라면 False Return
    if visited[start] == True:
        return False
    
    # 현재 Node 방문 처리
    visited[start] = True

    # 이웃노드 중
    for x in graph[start]:
        # 방문하지 않은 노드만 접근
        if visited[x] == False:
            dfs(x)
            
    return True
    
    
# 입력
N, M = map(int, input().split())
sys.setrecursionlimit(N*M)
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

# 노드 하나씩 보면서 덩어리 count
count = 0
for x in range(1, N+1):
    if not visited[x] and dfs(x):
        count += 1
        
print(count)