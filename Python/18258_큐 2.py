'''
===================================================================================================================================
문제
===================================================================================================================================
[18258] 큐 2
===================================================================================================================================
Log
===================================================================================================================================
' 2022-03-23-WED : 문제 파악
                   문제 해결
===================================================================================================================================
'''
'''
Algorithm
Queue 구현
1. 입력받을 때 readline().rstrip()으로 입력
2. push이면 append
3. pop이면 빈 리스트면 -1출력, 비어있지 않으면 del queue[0]
4. size이면 len(queue)
5. empty이면 빈 리스트면 1, 비어있지 않으면 0 출력
6. front이면 빈 리스트면 -1, 비어있지 않으면 print(queue[0])
7. back이면 빈 리스트면 -1, 비어있지 않으면 print(queue[-1])
'''

import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
queue = deque([])

for _ in range(N):
    order = input().rstrip()
    
    # order가 push이면
    if order[:4] == 'push':
        queue.append(int(order[5:]))
    # order가 pop이면
    elif order == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue[0])
            # del queue[0]
            queue.popleft()
    # order가 size이면
    elif order == 'size':
        print(len(queue))
    # order가 empty이면
    elif order == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    # order가 front이면
    elif order == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    # order가 back이면
    else:
        if not queue:
            print(-1)
        else:
            print(queue[-1])