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
1. 1부터 N까지의 숫자를 리스트에 하나씩 넣음
    ☞ 리스트에 i가 이미 들어있거나 리스트의 마지막 값보다 i가 작으면 무시
2. 리스트의 길이가 M이 되면 answer에 추가하고 리스트의 마지막 원소 확인
2.1. 리스트 마지막 원소가 N이 아니면 pop()한 번 하고 다음 index의 값 넣기
2.2. 리스트 마지막 원소가 N이면 끝에서부터 연속으로 작아지는 숫자의 개수만큼 pop하고 마지막 원소를 다음 index로 설정
3. answer 출력
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

N, M = map(int, input().split())
answer = []
temp = []
i = 1
while i < N+1:
    # i가 이미 temp에 들어있는 숫자보다 작으면 continue
    if temp and i < temp[-1]:
        i += 1
        continue
    
    # i가 이미 temp에 들어있으면 continue
    if i in temp:
        i += 1
        continue
    temp.append(i)
        
    # 수열의 길이가 M이 되면 break
    if len(temp) == M:
        answer.append(temp[:])
        
        # 마지막 원소가 마지막 숫자였다면
        if temp and temp[-1] == N:
            
            for j in range(N, 0, -1):
                # j를 마지막 원소로 설정
                i = temp[-1]
                # temp를 마지막 숫자부터 연속으로 들어있는 개수만큼 pop
                if temp and temp[-1] == j:
                    temp.pop()
                    if not temp:
                        break
                else:
                    break
            # temp가 비어있으면 break
            if not temp:
                break
            else: # 비어있지 않으면 temp의 마지막 원소를 i로 설정
                i = temp[-1]
                temp.pop()

        else:
            temp.pop()
    
    i += 1

for i in answer:
    for j in range(M):
        print(i[j], end = ' ')
    print()

answer = use_permutations(N, M)
for i in answer:
    for j in range(M):
        print(i[j], end = ' ')
    print()