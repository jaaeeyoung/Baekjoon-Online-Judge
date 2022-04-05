'''
===================================================================================================================================
문제
===================================================================================================================================
[14889] 스타트와 링크
===================================================================================================================================
Log
===================================================================================================================================
' 2022-04-06 WED : 문제 파악
                   시간 초과
                   문제 해결
===================================================================================================================================
'''
'''
Algorithm
back tracking - 재귀
1. start에 사람 번호 추가
2. 재귀함수 호출
3. 재귀함수가 return되면 pop
4. start의 길이가 N//2이면 능력치 구하고 차이 최솟값 갱신
'''

def back_tracking():
    global answer
    
    # start의 길이가 N//2이면 능력치 구하고 차이 최솟값 갱신
    if len(start) == N//2:
        s_start = 0
        s_link = 0
        for num1 in range(N):
            for num2 in range(N):
                if num1 < num2:
                    # 두 명 다 start 팀이면 s_start에 누적합
                    if num1 in start and num2 in start:
                        s_start += S[num1][num2] + S[num2][num1]
                    # 두명 다 start 팀에 없으면 s_link에 누적합
                    elif num1 not in start and num2 not in start:
                        s_link += S[num1][num2] + S[num2][num1]

        # 두 팀이 능력치 차의 최솟값 갱신
        if answer > max(s_start - s_link, s_link - s_start):
            answer = max(s_start - s_link, s_link - s_start)

    else:
        for num in range(N):
            # start 비어있으면 그냥 append
            if not start:
                start.append(num)
                # start[0]이 1이 되면break
                if start[0] == 1:
                    break
                back_tracking()
                start.pop()
            # start 비어있지 않으면 start에 들어있지 않고 start의 마지막 값보다 큰 값만 추가
            elif num not in start and num > start[-1]:
                start.append(num)
                # start[0]이 1이 되면break
                if start[0] == 1:
                    break
                back_tracking()
                start.pop()
                
import sys
input = sys.stdin.readline

N = int(input())
S = []
for _ in range(N):
    S.append(list(map(int, input().split())))

global answer
answer = 100*N*N
start = []
back_tracking()
print(answer)