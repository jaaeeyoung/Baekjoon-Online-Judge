'''
===================================================================================================================================
문제
===================================================================================================================================
[2792] 보석 상자
===================================================================================================================================
Log
===================================================================================================================================
' 2022-03-09-WED : 문제 파악
                   메모리 초과 -> 리스트 사용 줄여야될듯
                   student list 사용 x
                   7%에서 시간 초과
                   while문 조건을 보석 리스트의 마지막일 때 나가도록 조정
                   7%에서 시간 초과
                   UnboundLocalError : 함수 안에서 지역변수 초기화 안해줘서 생기는 오류,, ㅎㅎ
                   7%에서 시간 초과
                   Algorithm을 빼는 것이 아닌 나누는 것으로 변경
                   15% 틀렸습니다.
                   문제 해결
===================================================================================================================================
'''

'''
1. 이진 탐색 - 재귀 이용
2. 한 사람 당 나누어주는 보석의 최대 개수를 mid로 보고 mid의 최솟값 갱신
'''

import sys
input = sys.stdin.readline

# 이진 탐색 함수
def binary_search(start, end):
    global answer
    
    # 찾는 값이 없으면 None 반환
    if start > end:
        return None
    
    mid = (start + end) // 2
    
    # mid 값이 0이면 None 반환
    if mid == 0:
        return None
    
    # N 명의 학생에게 보석을 mid 개씩 나누어주기
    jewel_index = 0
    jewel = amount[0]
    student = 0
    flag = False # 가능하면 False, 불가능하면 True
    while student <= N:

        # 보석 나눠주기
        student += jewel // mid
        if jewel % mid > 0:
            student += 1
            jewel = 0

        # 모두 나누었을 때 학생 수가 N보다 커지면(보석이 남는 경우) 나가기
        if student > N:
            flag = True
            break
        
        # 보석 색상 index 증가
        jewel_index += 1
        # index가 보석 색상 리스트를 넘어가지 않으면
        if jewel_index < M:
            # jewel 값 갱신
            jewel = amount[jewel_index]
        else: # 넘어가면 break
            break
    
    if flag: # 보석이 남으면 더 많이씩 나누어줘야함
        return binary_search(mid + 1, end)
    else: # 가능한 경우 최솟값 찾기
        if answer > mid:
            answer = mid
        return binary_search(start, mid - 1)
        
        
# 입력
N, M = map(int, input().split())
amount = []
for _ in range(M):
    amount.append(int(input()))

answer = max(amount)
binary_search(1, max(amount))
print(answer)