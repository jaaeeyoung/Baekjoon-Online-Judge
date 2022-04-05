'''
===================================================================================================================================
문제
===================================================================================================================================
[15654] N과 M (5)
===================================================================================================================================
Log
===================================================================================================================================
' 2022-04-04-MON : 문제 파악
' 2022-04-05 TUE : 시간 초과
                   back tracking 사용
                   문제 해결
===================================================================================================================================
'''
'''
Algorithm
백트래킹 이용
1. 입력 리스트 오름차순 정렬
2. for문을 돌면서 stack에 없는 숫자 append
3. 재귀함수 호출
4. 재귀함수 return되면 pop
5. stack의 길이가 M이 되면 print
'''

def back_tracking():
    
    # stack의 길이가 M이 되면 print
    if len(stack) == M:
        print(' '.join(list(map(str, stack))))
    else:
        for num in nums:
            # num이 stack에 없으면 append
            if num not in stack:
                stack.append(num)
                back_tracking()
                stack.pop()

N, M = map(int, input().split())
nums = list(map(int, input().split()))

# 입력 수열 오름차순 정렬
nums.sort()
stack = []
back_tracking()

# stack = []
# answer = []
# index = 0
# flag = 0 # index 값이 변경된 적있으면 True
# while index < N+1:
    
#     # 해당 숫자가 스택에 이미 존재하면 continue
#     if index in stack:
#         index = (index+1)%N
#         continue
    
#     # 스택에 숫자 추가
#     stack.append(index)
    
#     # 스택의 길이가 M과 같으면 answer에 추가
#     if len(stack) == M:
#         answer.append(stack[:])
        
#         # stack의 값이 index의 역순과 동일하면 break
#         if stack[:] == list(range(N-1, N-1-M, -1)):
#             break
        
#         # stack의 마지막 값이 마지막 index이면 pop 2번
#         if stack[-1] == N-1:
#             stack.pop()
#             # stack이 비었으면 break
#             if not stack:
#                 break
#             # index 갱신 : stack에 없는 값이 나올 때 까지 변경
#             index = stack[-1]+1
#             while True:
#                 if index in stack[:-1]:
#                     index = (index + 1) % N
#                 else:
#                     break
#             stack.pop()
#             stack.append(index)
#             index = 0
#         elif N==M:
#             # 역순으로 정렬되어있는 곳까지 모두 pop()
#             i = len(stack) - 2
#             flag = False
#             while True:
#                 # 이전 index가 현재 index보다 작으면 pop
#                 if stack[i+1] < stack[i]:
#                     stack.pop()
#                 else: # 그렇지 않으면 index 저장하고 break
#                     stack.pop()
#                     # 위에 if문에 한 번도 안들어갔으면 index 변경하지 않음
#                     if len(stack) == M-1:
#                         break
#                     # index 갱신 : stack에 없는 값이 나올 때 까지 변경
#                     index = (stack[-1] + 1)%N
#                     while True:
#                         if index in stack[:-1]:
#                             index = (index+1)%N
#                         else:
#                             break
#                     flag = True
#                     stack.pop()
#                     stack.append(index)
#                     index = 0
#                     break
#                 i -= 1

#             # i가 변경되지 않았다면 index 갱신
#             if not flag:
#                 index = (stack[-1]+1)%N
#                 stack.pop()
#         else:
#             # index 1증가하고 pop
#             index = (index + 1)%N
#             stack.pop()
            
# for answer_nums in answer:
#     for index in answer_nums:
#         print(nums[index], end = ' ')
#     print()