'''
===================================================================================================================================
문제
===================================================================================================================================
[2798] 블랙잭
===================================================================================================================================
시간 및 메모리 제한
===================================================================================================================================
# 시간 제한 : 1 초
# 메모리 제한 : 128 MB
===================================================================================================================================
문제 설명
===================================================================================================================================
# 카지노에서 제일 인기 있는 게임 블랙잭의 규칙은 상당히 쉽다. 카드의 합이 21을 넘지 않는 한도 내에서, 카드의 합을 최대한 크게 만드는 게임
  이다. 블랙잭은 카지노마다 다양한 규정이 있다.

# 한국 최고의 블랙잭 고수 김정인은 새로운 블랙잭 규칙을 만들어 상근, 창영이와 게임하려고 한다.

# 김정인 버전의 블랙잭에서 각 카드에는 양의 정수가 쓰여 있다. 그 다음, 딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓는다. 그런 후에
  딜러는 숫자 M을 크게 외친다.

# 이제 플레이어는 제한된 시간 안에 N장의 카드 중에서 3장의 카드를 골라야 한다. 블랙잭 변형 게임이기 때문에, 플레이어가 고른 카드의 합은 
  M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.

# N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.
===================================================================================================================================
입력
===================================================================================================================================
# 첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다. 둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 이 값은 100,000을
  넘지 않는 양의 정수이다.

# 합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.
===================================================================================================================================
출력
===================================================================================================================================
# 첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력한다.
===================================================================================================================================
입출력 예
===================================================================================================================================
입력 1
5 21
5 6 7 8 9

출력 1
21

입력 2
10 500
93 181 245 214 315 36 185 138 216 295

출력 2
497
===================================================================================================================================
알고리즘 분류
===================================================================================================================================
# 브루트포스 알고리즘
===================================================================================================================================
Log
===================================================================================================================================
' 2022-02-12-SAT : 문제 파악
                   조합 - Itertools.combinations 사용
                   문제 해결
===================================================================================================================================
'''

# import itertools
 
# iterable = [1,2,3,4,5]
# result = itertools.permutations(iterable) # 순열
# result = itertools.product(iterable, repeat = 3) # 모든 조합 (반복 허용)
# result = itertools.combinations(iterable, r =3) # 조합
# for permutation in result:
#     print(permutation)

import itertools
import sys
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
cards = map(int, list(input().split()))
list_ = itertools.combinations(cards, r = 3) # 세 자리 조합 모두 찾기

max = 0
for i in list_: # 각 조합 중
    if sum(i) <= M and max < sum(i): # M을 넘지 않는 세 수의 합 중 최댓값 찾기
        max = sum(i)
        
print(max)