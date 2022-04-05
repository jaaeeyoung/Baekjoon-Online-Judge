'''
===================================================================================================================================
문제
===================================================================================================================================
[18290] NM과 K (1)
===================================================================================================================================
Log
===================================================================================================================================
' 2022-04-05 TUE : 문제 파악
                   2%에서 시간 초과
                   15%에서 런타임 에러
                   96%에서 틀렸습니다.
                   문제 해결
===================================================================================================================================
'''
'''
Algorithm
백트래킹 이용
1. graph 구현
2. 2중 for문을 돌면서 인접한 칸이 아니고 visited = False인 칸의 값을 stack에 append
3. append한 칸의 visited 값을 True로 변경하고 재귀함수 호출
4. 재귀함수 return되면 stack에서 pop하고 visited값 False로 변경
5. stack의 길이가 K가 되면 합을 구하고 합의 최댓값으로 갱신
'''

def back_tracking(x, y):
    global answer
    global sum_
    
    # stack의 길이가 K가 되면 합을 구하고 합의 최댓값 갱신
    if len(stack) == K:
        if answer < sum_:
            answer = sum_
    else:
        while x < N:
            while y < M:
                # stack이 비어있으면
                if not stack:
                    # (x, y)의 visited값이 False면 append
                    if not visited[x][y]:
                        stack.append((x, y))
                        visited[x][y] = True
                        sum_ += int(graph[x][y])
                        # 이 때의 x, y값을 인자로 재귀함수 호출
                        back_tracking(x, y)
                        # 재귀함수가 return되면 pop하고 visited False로 변경
                        stack.pop()
                        visited[x][y] = False
                        sum_ -= int(graph[x][y])
                    
                # (x, y)의 visited = False이고 인접한 칸이 아니면 append
                elif not visited[x][y] and (x-1, y) not in stack and (x+1, y) not in stack and (x, y-1) not in stack and (x, y+1) not in stack:
                    stack.append((x, y))
                    visited[x][y] = True
                    sum_ += int(graph[x][y])
                    # 이 때의 x, y값을 인자로 재귀함수 호출
                    back_tracking(x, y)
                    # 재귀함수가 return되면 pop하고 visited False로 변경
                    stack.pop()
                    visited[x][y] = False
                    sum_ -= int(graph[x][y])

                y = y + 1
            x = x + 1
            y = 0

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(input().rstrip().split())
    
global answer
global sum_
answer = -10000 * K - 1
sum_ = 0
stack = []
visited = [[False for _ in range(M)] for _ in range(N)]
back_tracking(0, 0)
print(answer)