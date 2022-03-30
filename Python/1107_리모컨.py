'''
===================================================================================================================================
문제
===================================================================================================================================
[1107] 리모컨
===================================================================================================================================
Log
===================================================================================================================================
' 2022-03-30-WED : 문제 파악
                   9%에서 틀렸습니다.
                   숫자키를 이용하지 않고 +, -키만 이용하는 경우의 수 확인
                   13%에서 틀렸습니다.
                   숫자키를 아무것도 사용할 수 없을 때 N > 100인 경우와 N < 100인 경우 모두 고려
                   36%에서 틀렸습니다.
                   answer 값 갱신할 때 M이 0일 때의 조건의 우선순위보다 +, -키만 눌러서 이동할 때의 조건의 우선순위를 먼저 고려
                   36%에서 틀렸습니다.
                   answer 값 갱신 첫 번째 조건에 길이 더하는 부분 추가
                   틀렸습니다.
                   answer 값 갱신 조건 순서 변경
                   85%에서 틀렸습니다.
                   answer 값 갱신 조건 중 첫 번째 조건에 이중 if문 추가
                   96%에서 틀렸습니다.
                   answer 값 갱신 조건 중 첫 번째 조건의 첫 번째 if문 조건 변경
                   문제 해결
===================================================================================================================================
'''
'''
Algorithm
완전 탐색 이용
1. 고장난 버튼을 제거하고 찾는 채널과 가장 가까운 수 만들기
2. 해당 숫자의 자리수 + (찾는 채널 - 만든 수) Return
'''

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
error_key = []
if M > 0:
    error_key = list(map(int, input().split()))
# 사용 가능한 키는 True, 그렇지 않으면 False
error_keys = dict()
for i in range(10):
    if i not in error_key:
        error_keys[i] = True
    else:
        error_keys[i] = False

# 보고싶은 채널과 가장 가까운 숫자 만들기
one_step = 5000011
# 찾는 채널보다 작은 수로 가까운 숫자 만들기
for num in range(N, -1, -1):
    # 찾는 채널이 100이거나 M이 0이거나 숫자가 모두 고장이면 break
    if N == 100 or M == 0 or M == 10:
        break
    
    # keys 중 error_key에 없는 숫자를 이용해 해당 숫자 만들 수 있으면 break
    temp = list(str(num))
    # error_key가 아닌 key 개수 세기
    count = 0
    for i in temp:
        if error_keys[int(i)]:
            count += 1
    # count가 temp의 길이와 같으면 만들 수 있는 숫자
    if count == len(temp):
        one_step = num
        break

# 찾는 채널보다 큰 수로 가까운 숫자 만들기
num = N
while True:
    # 찾는 채널이 100이거나 M이 0이거나 숫자가 모두 고장이면 break
    if N == 100 or M == 0 or M == 10:
        break
    
    # keys 중 error_key에 없는 숫자를 이용해 해당 숫자 만들 수 있으면 break
    temp = list(str(num))
    # error_key가 아닌 key 개수 세기
    count = 0
    for i in temp:
        if error_keys[int(i)]:
            count += 1
    # count가 temp의 길이와 같으면 만들 수 있는 숫자
    if count == len(temp):
        # 찾는 채널보다 작은 채널의 숫자 차이가 작으면 갱신
        if one_step < N:
            if N - one_step > num - N:
                one_step = num
                break
        else:
            one_step = num
            break
    
    if one_step < N and num - N >= N - one_step:
        break
    num += 1
# print('one_step:', one_step)
answer = 0
if N != 100:
    if M == 10 or one_step == 5000011:
        if M == 0:
            answer = min(max(100-N, N-100), len(str(N)))
        else:
            answer = max(N - 100, 100-N)
    # 100에서 +와 -만을 이용해 움직인 횟수가 one_step과의 차이보다 작으면 갱신
    elif max(100-N, N-100) < max(N-one_step, one_step-N) + len(str(N)):
        if one_step == 5000011:
            answer = min(max(100-N, N-100), len(str(N)))
        else:
            answer = max(100-N, N-100)
    # 숫자 중 고장난 키가 하나도 없으면 채널 번호 길이만큼 출력
    elif M == 0:
        answer = len(str(N))
    else:
        answer = len(str(one_step))
        answer += max(N - one_step, one_step - N)
print(str(answer))