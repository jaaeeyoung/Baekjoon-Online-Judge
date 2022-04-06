'''
===================================================================================================================================
문제
===================================================================================================================================
[2529] 부등호
===================================================================================================================================
Log
===================================================================================================================================
' 2022-04-06 WED : 문제 파악
                   문제 해결
===================================================================================================================================
'''
'''
Algorithm
back tracking - 재귀
1. 0부터 9까지 stack에 추가
1.1. stack이 비어있으면 바로 append
1.2. stack이 비어있지 않으면 stack이 없는 값이며 부등호를 확인해 < 이면 stack[-1]보다 큰 값, > 이면 stack[-1]보다 작은 값만 추가
2. 재귀함수 호출
3. 재귀함수 return되면 pop
4. stack의 길이가 K+1이 되면 최댓값, 최솟값 갱신
'''

def back_tracking():
    global min_
    global max_

    # stack의 길이가 k+1이 되면
    if len(stack) == k+1:
        num = int(''.join(list(map(str, stack))))
        # 최솟값 갱신
        if min_ > num:
            min_ = num
        # 최댓값 갱신
        if max_ < num:
            max_ = num

    else:
        for i in range(10):
            # stack 비어있으면 바로 추가
            if not stack:
                stack.append(i)
                back_tracking()
                stack.pop()
                
            # stack 비어있지 않으면
            elif i not in stack:
                if inequalities[len(stack)-1] == '<' and stack[-1] < i:
                # stack[-1]보다 큰 값만 추가
                    stack.append(i)
                    back_tracking()
                    stack.pop()
                elif inequalities[len(stack)-1] == '>' and stack[-1] > i:
                # stack[-1]보다 작은 값만 추가
                    stack.append(i)
                    back_tracking()
                    stack.pop()
                
import sys
input = sys.stdin.readline

k = int(input())
inequalities = list(input().rstrip().split())
global min_
global max_
min_ = 9876543211
max_ = 0
stack = []
back_tracking()

answer = ''
for i in range(k+1 - len(str(max_))):
    answer += '0'
answer += str(max_) + '\n'
for i in range(k+1 - len(str(min_))):
    answer += '0'
answer += str(min_)
print(answer)