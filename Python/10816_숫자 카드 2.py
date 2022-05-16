'''
===================================================================================================================================
문제
===================================================================================================================================
[10816] 숫자 카드 2
===================================================================================================================================
Log
===================================================================================================================================
' 2022-05-15 SUN : 문제 파악
                   문제 해결
===================================================================================================================================
'''
'''
Algorithm
1. 숫자 입력받을 때 Dictionary에 해당 숫자 개수 저장
2. M개 숫자에 대해 Dictionary의 value 출력
'''

# Dictionary 이용
N = int(input())
num_list = list(map(int, input().split()))
nums = {}
for num in num_list:
    if num not in nums:
        nums[num] = 1
    else:
        nums[num] += 1

M = int(input())
num_list = list(map(int, input().split()))
for num in num_list:
    if num in nums:
        print(nums[num], end = ' ')
    else:
        print(0, end = ' ')

# bisect 이용
import bisect

N = int(input())
num_list = list(map(int, input().split()))

# 오름차순 정렬
num_list.sort()

M = int(input())
lists = list(map(int, input().split()))

for num in lists:
    first = bisect.bisect_left(num_list, num)
    second = bisect.bisect_right(num_list, num)
    print(second-first, end = ' ')