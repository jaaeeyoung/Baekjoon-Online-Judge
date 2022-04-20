'''
===================================================================================================================================
문제
===================================================================================================================================
[20056] 마법사 상어와 파이어볼
===================================================================================================================================
Log
===================================================================================================================================
' 2022-04-20 WED : 문제 파악
                   문제 해결
===================================================================================================================================
'''
'''
Algorithm
구현
1. 리스트에 명령들 담음
2. 모든 파이어볼 이동
    -> graph에 각 칸마다 존재하는 파이어볼의 개수 갱신
3. 그래프 전체를 보면서 값이 2 이상인 경우 질량, 속력, 방향 계산해 명령을 담는 리스트에 추가
    -> 질량이 0이면 추가하지 않음
4. K번째 명령이 끝아면 질량의 총합 구함
'''

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
graph = [[[] for _ in range(N)] for _ in range(N)]
orders = []
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    orders.append((r-1, c-1, m, s, d))
    graph[r-1][c-1].append((m, s, d))

# 상, 우상향, 우, 우하향, 하, 좌하향, 좌, 좌상향
directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
for count in range(K):
    # 파이어볼 이동
    for r, c, m, s, d in orders:
        dx = directions[d][0] * s
        dy = directions[d][1] * s
        graph[r][c] = graph[r][c][1:]
        graph[(r+dx)%N][(c+dy)%N].append((m, s, d))
      
    orders = []
    for x in range(N):
        for y in range(N):
            # 파이어볼이 1개인 칸은 다음 명령에 추가
            if len(graph[x][y]) == 1:
                m, s, d = graph[x][y][0]
                orders.append((x, y, m, s, d))
            # 파이어볼이 2개 이상인 칸에서
            elif len(graph[x][y]) > 1:
                # 질량, 속력, 방향 구하기
                sum_m = 0
                sum_s = 0
                check_d = [0, 0]
                for m, s, d in graph[x][y]:
                    sum_m += m
                    sum_s += s
                    check_d[d%2] += 1
                    
                m = sum_m // 5
                # 질량이 0인 파이어볼 소멸
                if m == 0:
                    graph[x][y] = []
                    continue
                
                s = sum_s // len(graph[x][y])
                
                # 파이어볼 뱡향이 모두 홀수이거나 짝수이면 0, 2, 4, 6
                graph[x][y] = []
                if check_d[0] * check_d[1] == 0:
                    for d in range(0, 7, 2):
                        orders.append((x, y, m, s, d))
                        graph[x][y].append((m, s, d))
                else:
                    for d in range(1, 8, 2):
                        orders.append((x, y, m, s, d))
                        graph[x][y].append((m, s, d))

# graph에 있는 질량의 합 구하기
answer = 0
for x in range(N):
    for y in range(N):
        for m, s, d in graph[x][y]:
            answer += m
print(answer)