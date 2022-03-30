'''
===================================================================================================================================
문제
===================================================================================================================================
[14500] 테트로미노
===================================================================================================================================
Log
===================================================================================================================================
' 2022-03-30-WED : 문제 파악
                   2% 틀렸습니다.
                   고려하지 않음 도형 추가
                   문제 해결
===================================================================================================================================
'''
'''
Algorithm
완전 탐색 이용
1. 테트로미노의 모든 경우의 수마다 모든 좌표의 합을 구해 최댓값 갱신
    ☞ 테트로미노마다 회전과 대칭을 고려해야 함
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

max_sum = 0
# 1번 도형 확인
for i in range(N):
    for j in range(M-3):
        if board[i][j] + board[i][j+1] + board[i][j+2] + board[i][j+3] > max_sum:
            max_sum = board[i][j] + board[i][j+1] + board[i][j+2] + board[i][j+3]

# 1번 도형 회전 확인
for i in range(N-3):
    for j in range(M):
        if board[i][j] + board[i+1][j] + board[i+2][j] + board[i+3][j] > max_sum:
            max_sum = board[i][j] + board[i+1][j] + board[i+2][j] + board[i+3][j]

# 2번 도형 확인
for i in range(N-1):
    for j in range(M-1):
        if board[i][j] + board[i][j+1] + board[i+1][j] + board[i+1][j+1] > max_sum:
            max_sum = board[i][j] + board[i][j+1] + board[i+1][j] + board[i+1][j+1]

# 3번 도형, 3번 도형 변형, 4번 도형, 5번 도형 변형 확인
for i in range(N-2):
    for j in range(M-1):
        # 3번 도형
        if board[i][j] + board[i+1][j] + board[i+2][j] + board[i+2][j+1] > max_sum:
            max_sum = board[i][j] + board[i+1][j] + board[i+2][j] + board[i+2][j+1]
        # 3번 도형 180도 회전 도형
        if board[i][j] + board[i][j+1] + board[i+1][j+1] + board[i+2][j+1] > max_sum:
            max_sum = board[i][j] + board[i][j+1] + board[i+1][j+1] + board[i+2][j+1]
        # 3번 도형 오른쪽으로 270도 회전 도형
        if board[i][j] + board[i+1][j] + board[i+2][j] + board[i][j+1] > max_sum:
            max_sum = board[i][j] + board[i+1][j] + board[i+2][j] + board[i][j+1]
        # 3번 도형 좌우 대칭 도형
        if board[i][j+1] + board[i+1][j+1] + board[i+2][j+1] + board[i+2][j] > max_sum:
            max_sum = board[i][j+1] + board[i+1][j+1] + board[i+2][j+1] + board[i+2][j]
        # 4번 도형
        if board[i][j] + board[i+1][j] + board[i+1][j+1] + board[i+2][j+1] > max_sum:
            max_sum = board[i][j] + board[i+1][j] + board[i+1][j+1] + board[i+2][j+1]
        # 4번 도형 상하 대칭 도형
        if board[i][j+1] + board[i+1][j] + board[i+1][j+1] + board[i+2][j] > max_sum:
            max_sum = board[i][j+1] + board[i+1][j] + board[i+1][j+1] + board[i+2][j]
        # 5번 도형 오른쪽으로 90도 회전 도형
        if board[i][j+1] + board[i+1][j] + board[i+1][j+1] + board[i+2][j+1] > max_sum:
            max_sum = board[i][j+1] + board[i+1][j] + board[i+1][j+1] + board[i+2][j+1]
        # 5번 도형 오른쪽으로 270도 회전 도형
        if board[i][j] + board[i+1][j] + board[i+1][j+1] + board[i+2][j] > max_sum:
            max_sum = board[i][j] + board[i+1][j] + board[i+1][j+1] + board[i+2][j]

# 3번 도형 변형, 4번 도형 변형, 5번 도형, 5번 도형 변형 확인
for i in range(N-1):
    for j in range(M-2):
        # 3번 도형 오른쪽으로 90도 회전 도형
        if board[i][j] + board[i+1][j] + board[i][j+1] + board[i][j+2] > max_sum:
            max_sum = board[i][j] + board[i+1][j] + board[i][j+1] + board[i][j+2]
        # 3번 도형 상하 대칭 도형
        if board[i+1][j] + board[i+1][j+1] + board[i+1][j+2] + board[i][j+2] > max_sum:
            max_sum = board[i+1][j] + board[i+1][j+1] + board[i+1][j+2] + board[i][j+2]
        # 3번 도형 오른쪽으로 90도 회전 후 상하 대칭 도형
        if board[i][j] + board[i+1][j] + board[i+1][j+1] + board[i+1][j+2] > max_sum:
            max_sum = board[i][j] + board[i+1][j] + board[i+1][j+1] + board[i+1][j+2]
        # 3번 도형 오른쪽으로 90도 회전 후 좌우 대칭 도형
        if board[i][j] + board[i][j+1] + board[i][j+2] + board[i+1][j+2] > max_sum:
            max_sum = board[i][j] + board[i][j+1] + board[i][j+2] + board[i+1][j+2]
        # 4번 도형 오른쪽으로 90도 회전 도형
        if board[i][j+1] + board[i][j+2] + board[i+1][j] + board[i+1][j+1] > max_sum:
            max_sum = board[i][j+1] + board[i][j+2] + board[i+1][j] + board[i+1][j+1]
        # 4번 도형 오른쪽으로 90도 회전 후 좌우 대칭 도형
        if board[i][j] + board[i][j+1] + board[i+1][j+1] + board[i+1][j+2] > max_sum:
            max_sum = board[i][j] + board[i][j+1] + board[i+1][j+1] + board[i+1][j+2]
        # 5번 도형
        if board[i][j] + board[i][j+1] + board[i][j+2] + board[i+1][j+1] > max_sum:
            max_sum = board[i][j] + board[i][j+1] + board[i][j+2] + board[i+1][j+1]
        # 5번 도형 180도 회전 도형
        if board[i][j+1] + board[i+1][j] + board[i+1][j+1] + board[i+1][j+2] > max_sum:
            max_sum = board[i][j+1] + board[i+1][j] + board[i+1][j+1] + board[i+1][j+2]

print(max_sum)