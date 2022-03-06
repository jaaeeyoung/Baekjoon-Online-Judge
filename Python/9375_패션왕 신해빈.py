'''
===================================================================================================================================
문제
===================================================================================================================================
[9375] 패션완 신해빈
===================================================================================================================================
Log
===================================================================================================================================
' 2022-03-06-SUN : 문제 파악
                   메모리 초과
                   answer에 dict value의 합 미리 저장 후 itertools는 i가 2일 때부터 돌게함 -> 메모리 초과
                   입력받을 때 의상 이름 자리에 name으로 받았다가 _로 바꿈 -> 메모리 초과
                   itertools 안쓰는 알고리즘을 다시 짜야될듯
===================================================================================================================================
'''

'''
1. Dictionary로 입력 (key: 종류, value: 이름)
2. Dictionary의 value를 for문 돌면서 조합 수 구함
    -> itertools.combinations() 사용
4. 하나의 조합에 들어있는 수를 모두 곱해 answer에 누적합
'''
import itertools

# 리스트 원소의 곱을 반환하는 함수
def mul(list_):
    answer = 1
    for i in list_:
        answer *= i
    return answer

# 입력
T = int(input())
for _ in range(T):
    N = int(input())
    clothes = {}
    listn = []
    listk = []
    for _ in range(N):
        name , kind = input().split()
        listn.append(name)
        listk.append(kind)

    answer = N
    names= []
    kinds = []
    for i in range(2, N+1):
        tempn = []
        tempk = []
        for j in range(i):
            if listk[j] not in tempk and listn[j] not in tempn:
                tempn.append(listn[j])
                tempk.append(listk[j])
        # print(tempn)
        # print(tempk)
        if tempn not in names:
            names.append(tempn)
                
    print(names)
        # if kind not in clothes:
        #     clothes[kind] = 1
        # else:
        #     clothes[kind] += 1
    
    
    # 각 의상의 종류 별로 조합 수 구하기
    # answer = sum(clothes.values())
    # for i in range(2, len(clothes)+1):
    #     factorial(len)
    #     list_ = list(itertools.combinations(clothes.values(), i))
    #     for j in list_:
    #         answer += mul(j)
    # print(answer)