'''
===================================================================================================================================
문제
===================================================================================================================================
[14501] 퇴사
===================================================================================================================================
Log
===================================================================================================================================
' 2022-04-06 WED : 문제 파악
                   89%에서 틀렸습니다.
                   문제 해결
===================================================================================================================================
'''
'''
Algorithm
back tracking - 재귀
1. stack에 상담을 하는 날짜를 추가
1.1. stack이 비어있으면 오늘 날짜 추가
1.2. stack이 비어있지 않으면 T가 0이되는 날짜 추가
2. 재귀함수 호출
    -> date를 오늘 날짜 + T로 갱신하고 인자로 전달
3. 재귀함수가 return되면 이익 더하고 pop
4. date가 마지막 값면 수익의 최댓값 갱신
'''

def back_tracking(date):
    global answer
    global sum_
    
    # date가 마지막 값면 수익의 최댓값 갱신
    if date == N:
        if answer < sum_:
            answer = sum_
        date = 0
    else:
        while date < N:
            # stack이 비어있으면
            if not stack:
                # 일이 끝났을 때 N을 넘지 않으면 추가
                if date + info[date][0] <= N:
                    stack.append(date)
                    sum_ += info[date][1]
                    back_tracking(date + info[date][0])
                    stack.pop()
                    sum_ -= info[date][1]

            # stack이 비어있으면 일이 끝났을 때 N을 넘지 않으면 추가
            elif date + info[date][0] <= N:
                    stack.append(date)
                    sum_ += info[date][1]
                    back_tracking(date + info[date][0])
                    stack.pop()
                    sum_ -= info[date][1]
            date += 1
        back_tracking(N)
        

import sys
input = sys.stdin.readline

N = int(input())
info = []
for _ in range(N):
    info.append(list(map(int, input().split())))
stack = []
global answer
global sum_
answer = 0
sum_ = 0
back_tracking(0)
print(answer)