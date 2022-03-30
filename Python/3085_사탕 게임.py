'''
===================================================================================================================================
문제
===================================================================================================================================
[3085] 사탕 게임
===================================================================================================================================
Log
===================================================================================================================================
' 2022-03-30-WED : 문제 파악
                   문제 해결
===================================================================================================================================
'''
'''
Algorithm
완전 탐색 이용
'''

import sys
input = sys.stdin.readline

N = int(input())
board = []
for _ in range(N):
    board.append(list(input().rstrip()))

# 행을 기준으로 다른 색상 교환
max_count = 1
for i in range(N):
    for j in range(N-1):
        # 인접한 행의 색상이 다르면 교환
        if board[i][j] != board[i][j+1]:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            
            # 교환했을 때 사탕의 최대 개수 체크
            
            # 행 확인
            for x in range(N):
                count = 1
                for y in range(N-1):
                    # 인접한 행의 색상이 같으면 count 증가
                    if board[x][y] == board[x][y+1]:
                        count += 1
                        
                    else: # 같지 않으면 count 1로 초기화하고 다음 칸 확인
                        if max_count < count:
                            max_count = count
                        count = 1
                        continue
                    
                    if max_count < count:
                        max_count = count
                        
            # 열 확인
            for y in range(N):
                count = 1
                for x in range(N-1):
                    # 인접한 열의 색상이 같으면 count 증가
                    if board[x][y] == board[x+1][y]:
                        count += 1
                        
                    else: # 같지 않으면 count 1로 초기화하고 다음 칸 확인
                        if max_count < count:
                            max_count = count
                        count = 1
                        continue
                    
                    if max_count < count:
                        max_count = count
                    
            # 교환했던 칸 원위치
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

# 열을 기준으로 다른 색상 교환
for j in range(N):
    for i in range(N-1):
    
        # 인접한 열의 색상이 다르면 교환
        if board[i][j] != board[i+1][j]:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

            # 교환했을 때 사탕의 최대 개수 체크
            # 행 확인
            for x in range(N):
                count = 1
                for y in range(N-1):
                    # 인접한 행의 색상이 같으면 count 증가
                    if board[x][y] == board[x][y+1]:
                        count += 1
                        
                    else: # 같지 않으면 count 1로 초기화하고 다음 칸 확인
                        if max_count < count:
                            max_count = count
                        count = 1
                        continue
                    
                    if max_count < count:
                        max_count = count
            
            # 열 확인
            for y in range(N):
                count = 1
                for x in range(N-1):
                    # 인접한 열의 색상이 같으면 count 증가
                    if board[x][y] == board[x+1][y]:
                        count += 1
                    else: # 같지 않으면 count 1로 초기화하고 다음 칸 확인
                        if max_count < count:
                            max_count = count
                        count = 1
                        continue
                    
                    if max_count < count:
                        max_count = count
                    
            # 교환했던 칸 원위치
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(max_count)