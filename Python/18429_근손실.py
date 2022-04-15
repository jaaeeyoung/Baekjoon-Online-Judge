'''
===================================================================================================================================
문제
===================================================================================================================================
[18429] 근손실
===================================================================================================================================
Log
===================================================================================================================================
' 2022-04-15 FRI : 문제 파악
                   문제 해결
===================================================================================================================================
'''
'''
Algorithm
Back Tracking
1. stack에 운동 키트 추가
    ☞ stack에 들어있지 않은 숫자만 추가
2. 운동 키트 적용 직후 중량 갱신
3. 재귀함수 호출
4. 재귀함수 return되면 중량 원상복구 후 pop
5. stack의 길이가 N이 되거나 중량이 500 미만이 되면 pop먼저 할 수 있도록 구현
'''

def back_tracking(now_weight):
    global answer
    
    # stack의 길이가 N이 되거나 중량이 500 미만이 되면 POP먼저 하도록 구현
    if len(stack) == N or now_weight < 500:
        pass
    else:
        for idx in range(N):
            if idx not in stack:
                stack.append(idx)
                # 중량 계산
                now_weight = now_weight - K + weights[idx]
                # 마지막 index이고 중량이 500이상이면 answer 증가
                if len(stack) == N and now_weight >= 500:
                    answer += 1
                back_tracking(now_weight)
                stack.pop()
                now_weight = now_weight + K - weights[idx]

N, K = map(int, input().split())
weights = list(map(int, input().split()))
stack = []
global answer
answer = 0
now_weight = 500
back_tracking(now_weight)
print(answer)