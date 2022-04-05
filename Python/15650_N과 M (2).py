'''
===================================================================================================================================
문제
===================================================================================================================================
[15650] N과 M (2)
===================================================================================================================================
Log
===================================================================================================================================
' 2022-04-04-MON : 문제 파악
                   틀림
                   itertools로 구현했을 때 문제 해결
                   -> 백트래킹으로 구현해보기
                   백트래킹으로 구현했을 때 문제 해결
                   문제 해결
===================================================================================================================================
'''
'''
Algorithm
itertools 사용
1. itertools 라이브러리의 permutation() 이용해 1부터 N까지의 숫자 중 M개 선택해 모두 리스트에 저장
2. 리스트 오름차순 정렬
3. 각 원소들이 오름차순으로 정렬되어있는 순열만 answer에 저장해 출력

백트래킹 사용
1. stack이 비어있는지 확인
1.1. stack 비어있으면 stack에 num 추가하고 재귀함수 호출 후 재귀함수 return되면 pop
1.2. stack 비어있지 않으면 stack에 없는 값 중 stack의 마지막 숫자보다 큰 수 append하고 재귀함수 호출 후 재귀함수 return되면 pop
2. stack의 길이가 M과 같으면 stack print
'''

from itertools import permutations
def use_permutations(N, M):
    answer_in_func = []
    temp = list(permutations(range(1, N+1), M))
    temp.sort()
    for i in temp:
        flag = False
        for j in range(1, M):
            if i[j-1] > i[j]:
                flag = True
        if not flag:
            answer_in_func.append(i)
    return answer_in_func

def back_tracking():
    
    # stack의 길이가 M이면 print
    if len(stack) == M:
        print(' '.join(list(map(str, stack))))
    else:
        for num in range(1, N+1):
            # stack이 비어있으면
            if not stack:
                # stack에 num 추가
                stack.append(num)
                # 재귀함수 호출
                back_tracking()
                # 재귀함수 return되면 pop
                stack.pop()
            # 스택이 비어있지 않으면
            # num이 stack에 없고 num이 stack의 마지막 숫자보다 크면
            elif num not in stack and num > stack[-1]:
                # stack에 num 추가
                stack.append(num)
                # 재귀함수 호출
                back_tracking()
                # 재귀함수 return되면 pop
                stack.pop()
                
N, M = map(int, input().split())
stack = []
back_tracking()

# answer = use_permutations(N, M)
# for i in answer:
#     for j in range(M):
#         print(i[j], end = ' ')
#     print()