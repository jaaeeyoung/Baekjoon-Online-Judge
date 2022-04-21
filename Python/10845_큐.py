'''
===================================================================================================================================
문제
===================================================================================================================================
[10844] 큐
===================================================================================================================================
Log
===================================================================================================================================
' 2022-04-20 WED : 문제 파악
                   문제 해결
===================================================================================================================================
'''
'''
Algorithm
구현 - Simulation, Queue
'''

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
queue = deque()
for _ in range(N):
    orders = input().rstrip()
    
    # orders에 공백이 포함되어있으면 나누기
    if ' ' in orders:
        order, num = orders.split()
        num = int(num)
    else:
        order = orders
        
    if order == 'push':
        queue.append(num)
    elif order == 'pop':
        # 정수가 없는 경우
        if not queue:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()
    elif order == 'size':
        print(len(queue))
    elif order == 'empty':
        # 비어있으면 1
        if not queue:
            print(1)
        else:
            print(0)
    elif order == 'front':
        # 큐에 정수가 없으면 -1 출력
        if not queue:
            print(-1)
        else:
            print(queue[0])
    else:
        # 큐에 정수가 없으면 -1 출력
        if not queue:
            print(-1)
        else:
            print(queue[-1])