'''
===================================================================================================================================
문제
===================================================================================================================================
[2343] 기타 레슨
===================================================================================================================================
Log
===================================================================================================================================
' 2022-03-09-WED : 문제 파악
                   틀렸습니다.
===================================================================================================================================
'''

'''
1. 이진 탐색 - 재귀 이용
2. mid를 블루레이 크기로 두고 mid를 넘는 순간 다음 index에 동영상 저장
'''

import sys
input = sys.stdin.readline

# 이진 탐색 함수
def binary_search(start, end):
    global answer
    
    # 찾는 값이 없으면 None Return
    if start > end:
        return None
    
    mid = (start + end) // 2
    
    # 강의를 하나씩 더하면서 mid를 넘으면 다음 강의부터는 다음 blueray에 저장
    blueray = [0]
    for i in range(len(length)):

        blueray[-1] += length[i]
        # 현재 Blueray의 값이 mid를 넘으면 다음 Blueray로 index 변경
        if blueray[-1] >= mid and i != len(length) - 1:
            blueray.append(0)
            
    # 들어가지 않은 동영상이 있으면 mid 값 높여 다시 탐색
    if len(blueray) > M:
        return binary_search(mid + 1, end)
    else: # 정상적이라면 mid 최솟값 갱신
        if answer > max(blueray):
            answer = max(blueray)
        return binary_search(start, mid - 1)
        
# 입력
N, M = map(int, input().split())
length = list(map(int, input().split()))

answer = sum(length)
binary_search(1, answer)
print(answer)