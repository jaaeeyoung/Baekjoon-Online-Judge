'''
===================================================================================================================================
문제
===================================================================================================================================
[10972] 다음 순열
===================================================================================================================================
Log
===================================================================================================================================
' 2022-04-07 THU : 문제 파악
                   back tracking - 재귀 이용
                   런타임 에러(RecursionError)
                   런타임 에러(OverflowError)
                   그리디 이용
                   99%에서 런타임 에러 (IndexError)
                   N이 1일때 처리
                   문제 해결
===================================================================================================================================
'''
'''
Algorithm
back tracking - 재귀
1. stack에 입력으로 주어지는 순열을 넣은 상태로 시작
2. stack에 숫자 추가
2.1. stack이 비어있으면 바로 추가
2.2. stack이 비어있지 않으면 stack에 없는 숫자 추가
3. 재귀함수 호출
4. 재귀함수 return되면 pop
5. stack의 길이가 N이 되면 출력
'''

N = int(input())
nums = list(map(int, input().split()))

# 한자리숫자이면 -1 출력
if N == 1:
    print(-1)
# nums의 마지막 숫자가 N보다 작으면 끝에서부터 1씩 증가하는 부분 모두 pop
elif nums[-1] < N:
    for index in range(N-1, 0, -1):
        if nums[index-1] > nums[index]:
            nums.pop()
            # nums의 길이가 1인데 값이 N이면 -1출력
            if len(nums) == 1 and nums[0] == N:
                print(-1)
                break
        else:
            break
    nums.pop()
    # nums가 빈 리스트가 아니면
    if nums:
        # 다음에 올 숫자 저장
        num = (nums[-1] + 1) % (N + 1)
        if num == 0:
            num += 1
        # 이미 포함되어있는 숫자인지 확인
        while num in nums:
            if num in nums:
                num = (num + 1) % (N+1)
        
        nums.pop()
        nums.append(num)
        
        for num in range(1, N+1):
            if num not in nums:
                nums.append(num)
        print(' '.join(list(map(str, nums))))
# nums의 마지막 숫자가 N이면 2번 pop
else:
    nums.pop()
    num = (nums[-1]+1)%(N+1)
    if num == 0:
            num += 1
    # 이미 포함되어있는 숫자인지 확인
    while num in nums:
        if num in nums:
            num = (num + 1) % (N+1)

    nums.pop()
    nums.append(num)

    # 숫자를 1부터 N까지 확인하면서 들어있지 않은 숫자이면 append
    for num in range(1, N+1):
        if num not in nums:
            nums.append(num)
    print(' '.join(list(map(str, nums))))