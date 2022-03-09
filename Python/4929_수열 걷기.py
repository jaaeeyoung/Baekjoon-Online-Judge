'''
===================================================================================================================================
문제
===================================================================================================================================
[4929] 수열 걷기
===================================================================================================================================
Log
===================================================================================================================================
' 2022-03-10-THU : 문제 파악
                   문제 해결
===================================================================================================================================
'''
'''
Algorithm
이진 탐색 - bisect
1. bisect를 이용해 수열1과 수열2의 같은 값 찾기
2. 같은 수를 찾으면 각 수열에서 해당 숫자 이전까지의 합 구하기
3. answer에 각 수열의 합 중 최댓값 저장
'''

import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

while True:
    # 입력
    sequence1 = list(map(int, input().split()))
    # 0이 하나 주어지면 break
    if sum(sequence1) == 0:
        break
    seq1_len = sequence1[0]
    sequence1 = sequence1[1:]
    sequence2 = list(map(int, input().split()))
    seq2_len = sequence2[0]
    sequence2 = sequence2[1:]

    answer = 0
    index1 = 0 # 수열 1의 동일한 숫자의 index
    index2 = 0 # 수열 2의 동일한 숫자의 index
    for num in sequence1:
        # 동일한 숫자가 있으면
        if bisect_right(sequence2, num) - bisect_left(sequence2, num) > 0:
            # 첫 번째 수열의 해당 숫자까지의 합
            sum_seq1 = sum(sequence1[index1:bisect_right(sequence1, num)])
            # 두 번째 수열의 해당 숫자까지의 합
            sum_seq2 = sum(sequence2[index2:bisect_right(sequence2, num)])
            
            # 각 수열의 누적합 중 큰 값을 answer에 누적합
            answer += max(sum_seq1, sum_seq2)
            
            # 각 수열의 inex 갱신
            index1 = bisect_right(sequence1, num)
            index2 = bisect_right(sequence2, num)

    # 마지막 길의 최댓값 구해 answer에 추가
    answer += max(sum(sequence1[index1:]), sum(sequence2[index2:]))
    print(answer)
