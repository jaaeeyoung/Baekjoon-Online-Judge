'''
===================================================================================================================================
문제
===================================================================================================================================
[15652] N과 M (4)
===================================================================================================================================
Log
===================================================================================================================================
' 2022-04-04-MON : 문제 파악
                   문제 해결
===================================================================================================================================
'''
'''
Algorithm
백트래킹 사용
1. 1부터 N까지의 숫자를 리스트에 하나씩 넣음
    -> 현재 숫자가 리스트의 마지막 원소보다 작으면 무시
2. 리스트의 길이가 M이 되면 answer에 추가하고 리스트의 마지막 원소 확인
2.1. 리스트 마지막 원소가 N이 아니면 pop()한 번 하고 다음 index의 값 넣기
2.2. 리스트 마지막 원소가 N이면 끝에서부터 연속으로 N이 들어있는 개수만큼 pop하고 마지막 원소를 다음 index로 설정
3. answer 출력
'''

N, M = map(int, input().split())

temp = []
answer = []
num = 1
while num < N+1:
    # 해당 숫자가 temp의 마지막 원소보다 작으면 continue
    if temp and num < temp[-1]:
        num += 1
        continue
    
    # temp에 num 추가
    temp.append(num)
    
    # temp의 길이가 M이 되면
    if len(temp) == M:
        # answer에 temp 저장
        answer.append(temp[:])
        
        # 마지막 원소 확인
        if temp[-1] == N: # 마지막 원소가 N이면
            # 마지막 원소가 N이 아닐 때까지 pop
            while temp and temp[-1] == N:
                temp.pop()
            if temp:
                num = temp[-1]+1
                temp.pop()
                temp.append(num)
            else:
                break
            num = 1
        else: # 마지막 원소가 N이 아니면
            # num값 갱신하고 한번만 pop
            num = temp[-1] + 1
            temp.pop()

for nums in answer:
    for num in nums:
        print(num, end = ' ')
    print()