'''
===================================================================================================================================
문제
===================================================================================================================================
[11723] 집합
===================================================================================================================================
Log
===================================================================================================================================
' 2022-04-12 TUE : 문제 파악
                   문제 해결
===================================================================================================================================
'''
'''
Algorithm
구현 - Simulation
문제에 따라서 진행
'''

import sys
input = sys.stdin.readline

M = int(input())
S = []
for _ in range(M):
    orders = input().rstrip()
    
    # add x 이면 S에 x 추가
    if orders[:3] == 'add':
        order, x = orders.split()
        # S에 이미 x가 있는 경우 연산 무시
        if int(x) in S:
            continue
        S.append(int(x))
    
    # remove x : S에서 x를 제거
    elif orders[:6] == 'remove':
        order, x = orders.split()
        # S에 x가 없는 경우 연산 무시
        if int(x) not in S:
            continue
        S.remove(int(x))
    
    # check x : S에 x가 있으면 1, 없으면 0 반환
    elif orders[:5] == 'check':
        order, x = orders.split()
        if  int(x) in S:
            print(1)
        else:
            print(0)
            
    # toggle x : S에 x가 있으면 x 제거, 없으면 x 추가
    elif orders[:6] == 'toggle':
        order, x = orders.split()
        if int(x) in S:
            S.remove(int(x))
        else:
            S.append(int(x))
            
    # all : S를 {1, 2, ... , 20}으로 변환
    elif orders == 'all':
        S = list(range(1, 21))
    
    # empty : S를 공집합으로 변경
    elif orders == 'empty':
        S = []