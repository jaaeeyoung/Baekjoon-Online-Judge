'''
===================================================================================================================================
문제
===================================================================================================================================
[2108] 통계학
===================================================================================================================================
Log
===================================================================================================================================
' 2022-03-03-THU : 문제 파악
                   문제 해결
===================================================================================================================================
'''
'''
1. 각 숫자를 리스트에 저장
    -> 음수값 나오는지 확인
2. 산술평균 = floor(sum(리스트) /N)
3. 중앙값 = 리스트 오름차순 정렬 후 list[N/2]
4. 최빈값 = 각 숫자들을 입력받을 때 Dictionary에 등장횟수와 함께 저장하고 value가 가장 큰 key를 출력
5. 범위 = 리스트[-1] - 리스트[0]
'''

import sys
input = sys.stdin.readline

# 입력
N = int(input())
nums = []
nums_dict = {}
for _ in range(N):
    num = int(input())
    nums.append(num)
    if num not in nums_dict:
        nums_dict[num] = 1
    else:
        nums_dict[num] += 1

# 산술평균
print(round(sum(nums)/N))

# 중앙값
nums.sort()
print(nums[N//2])

# 최빈값
max_ = max(nums_dict.values()) # 최대 등장 횟수 찾기
temp = []
for key, value in nums_dict.items():
    if value == max_: # value가 최대 등장 횟수와 같은 숫자 따로 빼두기
        temp.append(key)

# 최빈 값이 여러 개 인 경우
if len(temp) != 1:
    # 정렬 후 두 번째로 작은 값 출력
    temp.sort()
    print(temp[1])
else:
    print(temp[0])
    
# 범위
print(nums[-1] - nums[0])