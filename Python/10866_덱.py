'''
===================================================================================================================================
문제
===================================================================================================================================
[10866] 덱
===================================================================================================================================
Log
===================================================================================================================================
' 2022-05-12 THU : 문제 파악
                   문제 해결
===================================================================================================================================
'''
'''
Algorithm
Dequeue, 구현-Simulation
'''

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
queue = deque()
for _ in range(N):
    order = input().rstrip()
    # 빈칸이 들어있으면 명령어와 숫자 분리
    if ' ' in order:
        order, num = order.split()
        num = int(num)
    
    if order == 'push_front':
        queue.appendleft(num)
    elif order == 'push_back':
        queue.append(num)
    elif order == 'pop_front':
        # 덱에 들어있는 정수가 없는 경우 -1 출력
        if not queue:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()
    elif order == 'pop_back':
        # 덱에 들어있는 정수가 없는 경우 -1 출력
        if not queue:
            print(-1)
        else:
            print(queue[-1])
            queue.pop()
    elif order == 'size':
        print(len(queue))
    elif order == 'empty':
        # 덱이 비어있으면 1, 비어있지 않으면 0 출력
        if not queue:
            print(1)
        else:
            print(0)
    elif order == 'front':
        # 덱에 들어있는 정수가 없는 경우 -1 출력
        if not queue:
            print(-1)
        else:
            print(queue[0])
    else:
        # 덱에 들어있는 정수가 없는 경우 -1 출력
        if not queue:
            print(-1)
        else:
            print(queue[-1])