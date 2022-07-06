'''
===================================================================================================================================
문제
===================================================================================================================================
[18111] 마인크래프트
===================================================================================================================================
Log
===================================================================================================================================
' 2022-07-05 TUE : 문제 파악
                   1%에서 틀렸습니다.
                   1%에서 시간 초과
                   문제 해결
===================================================================================================================================
'''
'''
Algorithm
구현
1. 기준 높이보다 높은 블럭의 차이 모두 합하기
2. 기준 높이보다 낮은 블럭의 차이 모두 합하기
3. 기준 높이만큼 쌓을 수 있는 블럭이 존재하면 answer 갱신
'''

import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

max_height = 0
min_height = 256
for x in range(len(graph)):
    for y in graph[x]:
        max_height = max(max_height, y)
        min_height = min(min_height, y)

answer = [(256*2+256)*M*N, max_height]
height = max_height
while height >= min_height:
    # 기준 높이보다 높은 블럭의 차이 모두 합하기
    # 기준 높이보다 낮은 블럭의 차이 모두 합하기
    tall = 0
    short = 0
    for x in range(len(graph)):
        for y in range(len(graph[x])):
            if graph[x][y] > height:
                tall += (graph[x][y] - height)
            elif graph[x][y] < height:
                short += (height - graph[x][y])

    # 기준 높이만큼 쌓을 수 있는 블록이 충분히 존재하면 answer 갱신
    if (B+tall) >= short:
        if answer[0] > tall * 2 + short:
            answer = [tall * 2 + short, height]
    
    # 기준 높이를 낮춰 재검사
    height -= 1
        
print(answer[0], answer[1])