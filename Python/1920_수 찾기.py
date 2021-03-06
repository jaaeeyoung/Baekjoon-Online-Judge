'''
===================================================================================================================================
문제
===================================================================================================================================
[1920] 수 찾기
===================================================================================================================================
Log
===================================================================================================================================
' 2022-03-08-TUE : 문제 파악
                   문제 해결
===================================================================================================================================
'''

'''
1. bisect 사용
2. A List sort
3. bisect_left와 bisect_right의 값을 비교해 같으면 0, 다르면 1 출력
'''

import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

# 입력
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

# A 정렬
A.sort()
for i in B:
    left = bisect_left(A, i)
    right = bisect_right(A, i)
    
    # left와 right의 값이 다르면 존재한다는 의미 -> 1 출력
    if left != right:
        print(1)
    else: # 값이 같으면 존재하지 않는다는 의미 -> 0 출력
        print(0)