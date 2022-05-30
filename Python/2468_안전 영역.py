'''
===================================================================================================================================
문제
===================================================================================================================================
[2468] 안전 영역
===================================================================================================================================
Log
===================================================================================================================================
' 2022-05-30-MON : 문제 파악
                   76% 틀렸습니다.
                   비의 양 0도 확인
                   문제 해결
===================================================================================================================================
'''

'''
DFS
1. 높이 정보 그래프 구현
2. dfs를 이용해 잠기지 않는 지역의 덩어리 구하기
3. 최댓값 출력
'''

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(x, y, amount_of_rain):
    
    # 위치를 벗어나면 return
    if x < 0 or x > N-1 or y < 0 or y > N-1:
        return False
    
    # 방문한 기록 있거나 높이가 비의 양보다 작거나 같으면 return
    if visited[x][y] or height_info[x][y] <= amount_of_rain:
        return False
    
    # 방문 기록
    visited[x][y] = True
    
    # 주변 노드 방문
    for dx, dy in dir:
        dfs(x+dx, y+dy, amount_of_rain)
    
    return True

N = int(input())
height_info = [list(map(int, input().split())) for _ in range(N)]

# 상, 하, 좌, 우
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# height_info의 최댓값 찾기
max_ = 0
for i in range(N):
    max_ = max(max_, max(height_info[i]))

answer = 0
for amount_of_rain in range(max_+1):
    count = 0 # 덩어리 개수
    visited = [[False for _ in range(N)] for _ in range(N)]
    
    # dfs 돌면서 비의 양보다 높은 곳만 접근했을 때의 덩어리 개수 구하기
    for x in range(len(height_info)):
        for y in range(len(height_info[i])):
            if dfs(x, y, amount_of_rain):
                count += 1
    answer = max(answer, count)

print(answer)