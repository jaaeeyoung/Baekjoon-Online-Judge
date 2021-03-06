'''
===================================================================================================================================
문제
===================================================================================================================================
[2217] 로프
===================================================================================================================================
Log
===================================================================================================================================
' 2022-02-14 MON : 문제 파악
                   시간 초과 -> for문 반복을 줄일 수 있도록 해야할 것 같음
' 2022-04-08 FRI : 그리디 알고리즘으로 구현
                   문제 해결
===================================================================================================================================
'''
'''
Algorithm
Greedy 이용
1. 각 로프의 중량을 리스트에 담아 sort
2. 1개 쓸 때부터 N개 쓸 때까지의 최댓값 구하기
    ☞ 각 최댓값은 [N-i] * i
'''

import sys
input = sys.stdin.readline

# 입력
N = int(input())
weights = []
for _ in range(N):
    weights.append(int(input()))

# 중량 리스트 오름차순 정렬
weights.sort()

# 로프 i개 쓸 때부터 N개 쓸 때까지 최댓값 갱신
max_weights = 0
for i in range(1, N+1):
    if max_weights < weights[N-i] * i:
        max_weights = weights[N-i] * i
print(max_weights)