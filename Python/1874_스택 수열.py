'''
===================================================================================================================================
문제
===================================================================================================================================
[1874] 스택 수열
===================================================================================================================================
Log
===================================================================================================================================
' 2022-03-21-MON : 문제 파악
                   시간 초과
===================================================================================================================================
'''
'''
Algorithm
Stack 이용
1. 수열의 현재 숫자와 Stack의 마지막 값 비교
-> 수열의 현재 숫자 > stack[-1]이면 해당 숫자까지 push()
-> 수열의 현재 숫자 == stack[-1]이면 pop()
-> 그외의 상황은 NO 출력
'''

import sys
input = sys.stdin.readline

n = int(input())
list_ = []
for _ in range(n):
    list_.append(int(input()))

now = 0
answer = []
pop_list = []
flag = False
for num in list_:
    print('num:', num)
    print('now:', now)
    for temp in range(now, num): # 여기서 for문 들어가면 temp+1 == num 조건이 맞고 안들어가면 temp == num 조건이 맞는데 이 부분 수정해야함
        print('temp = ', temp)
        if temp not in pop_list:
            answer.append('+')
    print('temp:', temp)
    
    if temp+1 == num:
    # if now == num:
        pop_list.append(num)
        answer.append('-')
        now = num
        while True:
            now -= 1
            print('now:', now)
            if now not in pop_list:
                break
    elif temp+1 < num:
        print('temp:', temp, 'num:', num)
        flag = True
        break
    elif temp + 1 > num:
        now = num
        while True:
            now -= 1
            print('now:', now)
            if now not in pop_list:
                break
    print()

if flag:
    print('NO')
else:
    for i in answer:
        print(i)

# stack = []
# flag = False # 불가능한 경우 True
# answer = []
# i = 0
# pop_list = []
# num = 1
# while i < len(list_) - 1:
#     # stack 비어있으면 stack에 마지막으로 들어갔던 값 + 1 append
#     if not stack:
#         stack.append(num)
#         num += 1
        
#     for j in range(num, list_[i] + 1):
#         # pop list에 없는 원소만 추가
#         if j not in pop_list:
#             stack.append(j)
#             answer.append('+')
#             num += 1

#     if list_[i] == stack[-1]:
#         pop_list.append(stack[-1])
#         stack.pop()
#         answer.append('-')
#         i += 1
#     else:
#         flag = True
#         break

# # 출력
# if flag:
#     print('NO')
# else:
#     for i in answer:
#         print(i)