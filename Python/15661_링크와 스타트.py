'''
===================================================================================================================================
문제
===================================================================================================================================
[15661] 링크와 스타트
===================================================================================================================================
Log
===================================================================================================================================
' 2022-04-06 WED : 문제 파악
                   시간 초과
===================================================================================================================================
'''
'''
Algorithm
back tracking - 재귀
1. start에 숫자 추가
1.1. start가 비어있으면 그냥 추가
1.2. start가 비어있지 않으면 stack에 들어있지 않고 stack의 마지막 숫자보다 큰 숫자만 추가
2. append될 때마다 두 팀의 능력치 차이에 따라 answer 갱신
3. 재귀함수 호출
4. 재귀함수 return되면 pop
5. start의 길이가 N-1이 되면 append하기 전에 pop부터 하도록 구현
'''

import sys
input = sys.stdin.readline

def back_tracking(s_start, s_link):
    global answer
    
    # start 길이가 N - 1이 되면 append하기 전에 pop부터 하도록 구현
    if len(start) == N-1:
        pass
    else:
        for num in range(N):
            # start 비어 있으면 숫자 추가
            if not start:
                # start의 첫 번째 원소가 1이면 return
                if num == 1:
                    return answer
                start.append(num)

                # start에 값이 추가될 때마다 능력치 확인
                for i in start[:-1]:
                    s_start += (S[i][num] + S[num][i])
                for i in range(N):
                    if i not in start:
                        s_link -= (S[num][i] + S[i][num])

                # answer값 갱신
                if answer < max(s_start - s_link, s_link - s_start):
                    answer = max(s_start - s_link, s_link - s_start)

                # 재귀함수 호출하고 return되면 pop
                back_tracking(s_start, s_link)
                
                for i in start[:-1]:
                    s_start -= S[i][start[-1]] + S[start[-1]][i]
                for i in range(N):
                    if i not in start:
                        s_link += (S[num][i] + S[i][num])
                    
                start.pop()
            
            # start 비어있지 않으면 start에 들어있지 않고 start의 마지막 숫자보다 큰 값만 추가
            elif num not in start and start[-1] < num:
                start.append(num)

                for i in start[:-1]:
                    s_start += S[i][num] + S[num][i]
                for i in range(N):
                    if i not in start:
                        s_link -= (S[num][i] + S[i][num])

                # answer값 갱신
                if answer > max(s_start - s_link, s_link - s_start):
                    answer = max(s_start - s_link, s_link - s_start)

                # 재귀함수 호출하고 return되면 pop
                back_tracking(s_start, s_link)

                for i in start[:-1]:
                    s_start -= S[i][num] + S[num][i]
                for i in range(N):
                    if i not in start:
                        s_link += (S[num][i] + S[i][num])
                start.pop()
                
N = int(input())
S = []
temp = []
s_link = 0
for _ in range(N):
    temp = list(map(int, input().split()))
    S.append(temp)
    s_link += sum(temp)

start = []
global answer
answer = 100*N*N
s_start = 0
print(back_tracking(s_start, s_link))