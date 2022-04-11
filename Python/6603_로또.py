'''
===================================================================================================================================
문제
===================================================================================================================================
[6603] 로또
===================================================================================================================================
Log
===================================================================================================================================
' 2022-04-11 MON : 문제 파악
                   문제 해결
===================================================================================================================================
'''
'''
Algorithm
Back Tracking 이용
1. 입력받은 수를 리스트로 저장
2. 리스트에 들어있는 숫자를 stack에 append
2.1. stack이 비어있으면 숫자 바로 추가
2.2. stack이 비어있지 않으면 stack의 마지막 숫자보다 큰 숫자 append
3. 재귀함수 호출
4. 재귀함수 return되면 stack pop
5. stack의 길이가 K와 같아지면 print
'''

def back_tracking():
    
    # stack의 길이가 K와 같아지면 print
    if len(stack) == 6:
        print(' '.join(list(map(str, stack))))
    else:
        for index in range(1, nums[0]+1):
            # stack 비어있으면 숫자 바로 추가
            if not stack:
                stack.append(nums[index])
                back_tracking()
                stack.pop()
            elif nums[index] > stack[-1]:
                stack.append(nums[index])
                back_tracking()
                stack.pop()

while True:
    nums = list(map(int, input().split()))
    if nums[0] == 0:
        break
    stack = []
    back_tracking()
    print()