'''
===================================================================================================================================
문제
===================================================================================================================================
[10971] 외판원 순회 2
===================================================================================================================================
Log
===================================================================================================================================
' 2022-04-10 SUN : 문제 파악
                   10%에서 시간 초과
                   50%에서 틀렸습니다
                   문제 해결
===================================================================================================================================
'''
'''
Algorithm
Back Tracking 이용
1. 입력으로 리스트로 저장해 graph 구현
2. stack에 값 추가
2.1. stack이 비어있으면 현재 숫자 바로 추가
2.2. stack이 비어있지 않으면 stack에 들어있지 않으면서 비용이 0 이상인 값만 추가
3. 재귀함수 호출
4. 재귀함수 호출되면 stack pop
5. stack의 길이가 N이 되면 시작지점으로 돌아올 수 있는지(비용이 0 이상인지) 확인
5.1. 시작지점으로 돌아올 수 있다면 최소비용 갱신
'''

def back_tracking(costs):
    global answer
    
    # stack의 길이가 N-1이 되면
    if len(stack) == N:
        # 시작지점으로 돌아올 수 있으면 최소 비용 갱신
        if graph[stack[-1]][stack[0]] > 0:
            costs += graph[stack[-1]][stack[0]]
            if answer > costs:
                answer = costs

    else:
        for num in range(N):
            # stack이 비어있으면
            if not stack:
                if num == 1:
                    return
                # 그냥 추가
                stack.append(num)
                back_tracking(costs)
                stack.pop()
            # stack이 비어있지 않으면 stack에 들어있지 않으면서 비용이 0 이상인 값만 추가
            elif num not in stack and graph[stack[-1]][num] > 0:
                stack.append(num)
                costs += graph[stack[-2]][stack[-1]]
                back_tracking(costs)
                costs -= graph[stack[-2]][stack[-1]]
                stack.pop()
                
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

global answer
answer = 1000000*N*N
stack = []
costs = 0
back_tracking(costs)
if answer == 1000000*N*N:
    print(0)
else:
    print(answer)