'''
===================================================================================================================================
문제
===================================================================================================================================
[11723] 집합
===================================================================================================================================
Log
===================================================================================================================================
' 2022-04-12 TUE : 문제 파악
                   8%에서 시간 초과
                   12%에서 틀렸습니다
                   문제 해결
===================================================================================================================================
'''
'''
Algorithm
Back Tracking
1. stack에 수열의 숫자 하나씩 추가
1.1. stack이 비어있으면 바로 append
1.2. stack이 비어있지 않으면 stack의 마지막 숫자보다 큰 숫자만 추가
2. stack 원소의 합이 S가 되면 ANSWER 1 증가
3. 재귀함수 호출
4. 재귀함수 return되면 pop
5. stack의 길이가 N이 되면 바로 append하지 못하도록 구현 
'''

def back_tracking(sum_):
    global answer
    
    # stack 길이가 N이 되면 POP먼저 하도록 구현
    if len(stack) == N:
        pass
    else:
        for idx in range(N):
            # stack 비어있으면 바로 append
            if not stack:
                stack.append(idx)
                sum_ += list_[idx]
                if sum_ == S:
                    answer += 1
                back_tracking(sum_)
                stack.pop()
                sum_ -= list_[idx]
                
            # stack 비어있지 않으면 들어있지 않은 숫자만 추가
            elif stack[-1] < idx:
                stack.append(idx)
                sum_ += list_[idx]
                if sum_ == S:
                    answer += 1
                back_tracking(sum_)
                stack.pop()
                sum_ -= list_[idx]
                
N, S = map(int, input().split())
list_ = list(map(int, input().split()))

global answer
answer = 0
sum_ = 0
stack = []
back_tracking(sum_)
print(answer)