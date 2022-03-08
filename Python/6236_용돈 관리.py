'''
===================================================================================================================================
문제
===================================================================================================================================
[6236] 용돈 관리
===================================================================================================================================
Log
===================================================================================================================================
' 2022-03-08-TUE : 문제 파악
                   문제 해결
===================================================================================================================================
'''

'''
1. 이진 탐색 - 재귀 이용
2. 인출해야하는 금액을 mid로 보고 mid가 최소가 되도록 갱신
'''

import sys
sys.stdin.readline

# 이진 탐색 함수
def binary_search(start, end):
    global answer
    
    # 찾는 값이 없으면 None 반환
    if start > end:
        return None
    
    mid = (start + end) // 2
    
    balance = 0 # 잔고
    count = 0 # 출금 횟수
    flag = False # 불가능하면 True, 가능하면 False
    for i in range(N):
        # 예외사항 : M번을 맞추기 위해 남은 금액이 그 날 사용할 금액보다 많아도 남은 금액은 통장에 집어넣고 다시 K원 인출
        if N - i == M - count: # 남은 날짜가 M - count와 같으면 나머지 날은 돈이 충분해도 모두 인출해야함
            # mid 값이 money에 들어있는 나머지 금액보다 크지만 않으면 가능함
            if max(money[i:]) <= mid:
                flag = False
                count = M
                break
        # 돈이 모자라면 남은 금액 통장에 넣고 K원 인출
        elif balance < money[i]:
            balance = mid - money[i]
            count += 1
        else: # 통장에서 뺀 돈으로 하루 보낼 수 있으면 그대로 사용
            balance -= money[i]
        
        # 잔고가 한 번이라도 음수가 나오면 불가능
        if balance < 0:
            flag = True
            break
    
    # 현재 mid값으로 불가능하면 mid 값 증가시켜 다시 탐색
    if flag or count > M:
        return binary_search(mid + 1, end)
    else: # 가능하면 mid의 최솟값 찾기
        if answer > mid and count == M:
            answer = mid
        return binary_search(start, mid - 1)
            

# 입력
N, M = map(int, input().split())
money = []
for _ in range(N):
    money.append(int(input()))

answer = sum(money)
binary_search(1, sum(money))
print(answer)