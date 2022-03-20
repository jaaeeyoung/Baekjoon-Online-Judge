'''
===================================================================================================================================
문제
===================================================================================================================================
[4949] 균형잡힌 세상
===================================================================================================================================
Log
===================================================================================================================================
' 2022-03-20-SUN : 문제 파악
                   문제 해결
===================================================================================================================================
'''
'''
Algorithm
Stack 이용
1. Stack을 생성
2. 문자가 ( 이거나 [ 인 경우 Stack에 추가, ) 이거나 ] 인 경우 stack의 마지막 원소가 ( 이거나 [ 인지 확인하고 맞은면 POP()
3. pop할 때 짝이 맞지 않으면 no
4. 스택에 원소가 남아있으면 no
'''

import sys
input = sys.stdin.readline

while True:
    words = input().rstrip()
    # 입력이 .이면 종료
    if words == '.':
        break
    
    stack = []
    flag = False # 균형이 맞으면 False, 균형이 맞지 않으면 True
    for word in words:
        # 문자가 (인 경우 소괄호 stack에 추가
        if word == '(':
            stack.append(word)
        elif word == ')': # 문자가 )인 경우 소괄호 stack에서 pop
            # stack의 마지막 원소와 짝이 맞으면 pop
            if stack and stack[-1] == '(': 
                stack.pop()
            # stack 비어있으면 no 출력
            else:
                flag = True
                break
                
        elif word == '[': # 문자가 [인 경우 대괄호 stack에 추가
            stack.append(word)
        elif word == ']': # 문자가 ]인 경우 대괄호 stack에서 pop
            # stack의 마지막 원소와 짝이 맞으면 pop
            if stack and stack[-1] == '[':
                stack.pop()
            # 대괄호 stack 비어있으면 no 출력
            else:
                flag = True
                break

    # flag가 True이거나 소괄호 stack과 대괄호 stack 중 비어있지 않은 리스트가 있으면 균형을 이루지 않는 문자열
    if flag or stack:
        print('no')
    # 소괄호 stack과 대괄호 stack에 아무것도 없으면 균형을 이루는 문자열
    elif not stack:
        print('yes')