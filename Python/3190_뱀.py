'''
===================================================================================================================================
문제
===================================================================================================================================
[3190] 뱀
===================================================================================================================================
Log
===================================================================================================================================
' 2022-03-31-THU : 문제 파악
                   문제 해결
===================================================================================================================================
'''
'''
Algorithm
구현 - 시뮬레이션
1. board를 리스트로 구현
    -> 사과가 있는 칸은 True, 사과가 없는 칸은 False
2. 현재 뱀의 몸이 닿아있는지 여부가 담긴 snake 리스트 구현
    -> 몸이 닿아있으면 True, 닿아있지 않으면 False
3. 반복문 1번 돌 때마다 snake의 다음 칸 True, 첫 번째 칸 False
    -> 사과 먹으면 첫 번째 칸 놔두기
4. 반복문 1번 돌 때마다 초 증가
    -> 초 == x+1이면 c의 방향으로 이동
    -> 현재 방향 (상, 하, 좌, 우) 저장해두고
    상일 때 D이면 우, L이면 좌로 변경
    하일 때 D이면 좌, L이면 우로 변경
    좌일 때 D이면 상, L이면 하로 변경
    우일 때 D이면 하, L이면 상으로 변경
5. 다음 칸의 snake가 True이거나 board 범위 벗어나면 break
'''

import sys
input = sys.stdin.readline

# 현재 방향과 변경할 방향으로 인자로 줬을 때 다음 방향을 return하는 함수
def return_index(index, C):
    # 현재 방향이 상인 경우
    if index == 0:
        # C가 D이면 우로 변경
        if C == 'D':
            index = -1
        # C가 L이면 좌로 변경
        else:
            index = 2
    # 현재 방향이 하인 경우
    elif index == 1:
        # C가 D이면 좌로 변경
        if C == 'D':
            index = 2
        # C가 L이면 우로 변경
        else:
            index = -1
    # 현재 방향이 좌인 경우
    elif index == 2:
        # C가 D이면 상으로 변경
        if C == 'D':
            index = 0
        # C가 L이면 하로 변경
        else:
            index = 1
    # 현재 방향이 우인 경우
    else:
        # C가 D이면 하로 변경
        if C == 'D':
            index = 1
        # C가 L이면 상으로 변경
        else:
            index = 0
    return index

# board 구현
N = int(input())
board = [[False for _ in range(N+1)] for _ in range(N+1)]
# 뱀 리스트 구현
snake = [[False for _ in range(N+1)] for _ in range(N+1)]

# 사과 위치 저장
K = int(input())
for _ in range(K):
    x, y = map(int, input().split())
    # 사과 위치 True로 변환
    board[x][y] = True

# 뱀의 방향 변환 정보 저장
L = int(input())
move = []
for _ in range(L):
    time, direction = input().split()
    move.append((int(time), direction))

# 방향 : 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
index = -1 # 현재 방향
x = 1 # 현재 위치
y = 1 # 현재 위치
# 현재 위치에 뱀 저장
snake[x][y] = True
snake_length = 1 # 뱀 길이
last_loc = [1, 1]
time = 1
index_record = []
while True:
    # 현재 시간이 X+1이면 C의 방향으로 방향 회전
    if move and time == move[0][0]+1:
        index = return_index(index, move[0][1])
        move = move[1:]
    
    # 현재 방향으로 이동
    nx = x+dx[index]
    ny = y+dy[index]
    
    # 다음 칸의 위치에 뱀의 몸이 있거나 board의 범위를 벗어나면 break
    if nx < 1 or nx > N or ny < 1 or ny > N or snake[nx][ny]:
        break
    
    index_record.append(index)
    
    # 다음 칸으로 뱀 이동
    snake[nx][ny] = True
    snake_length += 1
    # 사과가 있으면 사과 삭제
    if board[nx][ny]:
        board[nx][ny] = False
    else: # 사과가 없으면 첫 칸에서 뱀 삭제
        snake[last_loc[0]][last_loc[1]] = False
        snake_length -= 1

        last_loc[0] += dx[index_record[-snake_length]]
        last_loc[1] += dy[index_record[-snake_length]]
    
    # 시간 증가
    time += 1
    
    # x, y 갱신
    x = nx
    y = ny

print(time)