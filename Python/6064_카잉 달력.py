'''
===================================================================================================================================
문제
===================================================================================================================================
[6064] 카잉 달력
===================================================================================================================================
Log
===================================================================================================================================
' 2022-03-31-THU : 문제 파악
                   시간 초과
===================================================================================================================================
'''
'''
Algorithm
완전 탐색 이용
1. 현재 년도 1씩 증가
2. m, n 1씩 증가
    -> 각각 M, N과 같아지면 1로 초기화
3. x, y와 같아지면 현재 년도 출력
'''

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    m, n = 0, 0
    k = 0 # 현재 년도
    while True:
        k += 1

        # m이 M과 같아지면 1로 초기화
        if m == M:
            m = 1
        else: # 그렇지 않으면 1 증가
            m += 1
        
        # n이 N과 같아지면 1로 초기화
        if n == N:
            n = 1
        else: # 그렇지 않으면 1 증가
            n += 1
        
        # m == x이고 n == y이면 break
        if m == x and n == y:
            break
        
        # 마지막 해이면 k를 -1로 초기화하고 break
        if m == M and n == N:
            k = -1
            break
    print(k)