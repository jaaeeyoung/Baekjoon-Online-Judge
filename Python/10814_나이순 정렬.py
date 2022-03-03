'''
===================================================================================================================================
문제
===================================================================================================================================
[10814] 나이순 정렬
===================================================================================================================================
Log
===================================================================================================================================
' 2022-03-03-THU : 문제 파악
                   문제 해결
===================================================================================================================================
'''
'''
1. 나이와 이름을 튜플로 받아 리스트로 저장
2. lambda 함수를 이용해 나이순으로 정렬
    -> 나이가 같으면 이미 리스트에 저장되어 있던 순서대로 정렬되기 때문에 가입한 순으로 다시 정렬할 필요가 없음
'''

# 입력
N = int(input())
people = []
for _ in range(N):
    age, name = input().split()
    people.append((int(age), name))
    
# 나이순 정렬
people.sort(key = lambda x: x[0])
for i in people:
    print(i[0], i[1])