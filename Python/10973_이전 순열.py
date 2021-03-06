'''
===================================================================================================================================
문제
===================================================================================================================================
[10973] 이전 순열
===================================================================================================================================
Log
===================================================================================================================================
' 2022-04-08 FRI : 문제 파악
                   문제 해결
===================================================================================================================================
'''
'''
Algorithm
Greedy 이용
1. 입력 순열을 리스트로 받음
2. N이 1이거나 리스트가 오름차순 정렬되어있으면 -1 출력
3. 리스트의 마지막 숫자가 1보다 크면
3.1. 리스트의 끝에서부터 내림차순 정렬되어있는 부분 모두 pop
3.2. 리스트의 (마지막 숫자 - 1) % (N+1)을 저장하고 pop한 후 저장된 숫자 append
    ☞ (마지막 숫자 - 1) % (N+1)가 리스트 내에 존재하지 않아야 함
4. 리스트의 마지막 숫자가 1이면
4.1. pop하고 리스트의 (마지막 숫자 - 1) % (N+1)을 저장하고 pop한 후 저장된 숫자 append
    ☞ (마지막 숫자 - 1) % (N+1)가 리스트 내에 존재하지 않아야 함
5. 남은 자리수 stack에 포함되어있지 않은 값으로 채우기
'''

N = int(input())
stack = list(map(int, input().split()))

# N이 1이거나 리스트가 오름차순 정렬되어있으면 -1 출력
if N == 1 or stack == list(range(1, N+1)):
    print(-1)
else:
    # 리스트의 마지막 숫자가 1보다 크면
    if stack[-1] > 1:
        # 리스트의 끝에서부터 처음으로 가면서 내림차순 정렬되어있는 부분 모두 pop
        for index in range(N-1, 0, -1):
            if stack[index-1] < stack[index]:
                stack.pop()
            else:
                break
        stack.pop()
        
        # 다음에 들어가야할 숫자 저장
        next_num = (stack[-1] - 1) % (N+1)
        if next_num == 0:
            next_num = N-1
        while next_num in stack:
            next_num = (next_num - 1) % (N+1)
            if next_num == 0:
                next_num = N-1

        # 리스트의 마지막 원소를 새로운 숫자로 변경
        stack.pop()
        stack.append(next_num)
        
        # 리스트 나머지 자리 채우기
        for num in range(N, 0, -1):
            if num not in stack:
                stack.append(num)
    else:
        stack.pop()

        # 다음에 들어가야할 숫자 저장
        next_num = (stack[-1] - 1) % (N+1)
        if next_num == 0:
            next_num = N-1
        while next_num in stack:
            next_num = (next_num - 1) % (N+1)
            if next_num == 0:
                next_num = N-1

        # 리스트의 마지막 원소를 새로운 숫자로 변경
        stack.pop()
        stack.append(next_num)
        
        # 리스트 나머지 자리 채우기
        for num in range(N, 0, -1):
            if num not in stack:
                stack.append(num)

    print(' '.join(list(map(str, stack))))