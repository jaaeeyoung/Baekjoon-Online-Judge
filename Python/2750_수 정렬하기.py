'''
===================================================================================================================================
문제
===================================================================================================================================
[2750] 수 정렬하기
===================================================================================================================================
시간 및 메모리 제한
===================================================================================================================================
# 시간 제한 : 1 초
# 메모리 제한 : 128 MB
===================================================================================================================================
문제 설명
===================================================================================================================================
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
===================================================================================================================================
입력
===================================================================================================================================
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다.
# 수는 중복되지 않는다.
===================================================================================================================================
출력
===================================================================================================================================
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
===================================================================================================================================
입출력 예
===================================================================================================================================
입력
5
5
2
3
4
1

출력
1
2
3
4
5
===================================================================================================================================
알고리즘 분류
===================================================================================================================================
# 구현
# 정렬
===================================================================================================================================
Log
===================================================================================================================================
2022-02-11-FRI : 문제 파악
                 런타임 에러 (IndexError)
2022-02-12-SAT : 문제 해결
2022-02-27-SUN : 더 나은 방법으로 수정
                 -> 매번 최솟값을 찾아 출력하는 것이 아닌 애초에 sort()로 정렬하고 하나씩 출력하는 방식
===================================================================================================================================
'''

N = int(input())

# 입력
nums = []
for i in range(N):
    nums.append(int(input()))
    
# for i in range(N):
#     # nums에서 최솟값 출력 후
#     print(min(nums))
#     # 출력한 값 삭제
#     nums.remove(min(nums))

nums.sort()
for i in nums:
    print(i)