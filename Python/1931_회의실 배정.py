'''
===================================================================================================================================
문제
===================================================================================================================================
[1931] 회의실 배정
===================================================================================================================================
시간 및 메모리 제한
===================================================================================================================================
# 시간 제한 : 2 초
# 메모리 제한 : 128 MB
===================================================================================================================================
문제 설명
===================================================================================================================================
# 한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다. 각 회의 I에 대해 시작시간과 끝나는 시간
  이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 단, 회의는 한번 시작하면 중간에 중단될
  수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자
  마자 끝나는 것으로 생각하면 된다.
===================================================================================================================================
입력
===================================================================================================================================
# 첫째 줄에 회의의 수 N(1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N+1 줄까지 각 회의의 정보가 주어지는데 이것은 공백을 사이에 두고 회의의
  시작시간과 끝나는 시간이 주어진다. 시작 시간과 끝나는 시간은 2^31-1보다 작거나 같은 자연수 또는 0이다.
===================================================================================================================================
출력
===================================================================================================================================
# 첫째 줄에 최대 사용할 수 있는 회의의 최대 개수를 출력한다.
===================================================================================================================================
입출력 예
===================================================================================================================================
입력 1
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14

출력 1
4
===================================================================================================================================
힌트
===================================================================================================================================
# (1,4), (5,7), (8,11), (12,14) 를 이용할 수 있다.
===================================================================================================================================
알고리즘 분류
===================================================================================================================================
# 그리디 알고리즘
# 정렬
===================================================================================================================================
Log
===================================================================================================================================
' 2022-02-15-TUE : 문제 파악
                   시간 초과
===================================================================================================================================
'''

'''
Algorithm
1. 시간을 Tuple로 짝지어서 List로 만듦
2. Tuple의 앞 원소를 기준으로 오름차순 정렬
3. for문 돌면서 Tuple의 뒷 원소보다 앞 원소가 큰 Tuple 찾기
-> count 증가
4. While 문 돌면서 answer의 max값보다 I의 길이가 길면 break
5. While 문 모두 돌면 answer 중 max값 찾아 출력
'''

N = int(input())
I = []
for _ in range(N):
    I.append(tuple(map(int, input().split())))
    
# Tuple 앞 원소 기준으로 오름차순 정렬
I.sort()

answer = []
while True:
    now_end = 0 # 현재 미팅의 끝나는 시각
    count = 0 # 가능한 회의의 개수 담을 변수
    
    # 뒷 원소보다 앞 원소보다 큰 Tuple 찾기
    for i, j in I:
        if i >= now_end:
            now_end = j
            count += 1
    answer.append(count)

    I = I[1:] # 첫 번째 Tuple 삭제
    if len(I) < max(answer):
        break

print(max(answer))