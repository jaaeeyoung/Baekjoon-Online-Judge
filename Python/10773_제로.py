'''
===================================================================================================================================
문제
===================================================================================================================================
[10773] 제로
===================================================================================================================================
Log
===================================================================================================================================
' 2022-03-19-SAT : 문제 파악
                   문제 해결
===================================================================================================================================
'''

'''
1. 입력을 하나씩 받으면서 0이 아니면 append()
2. 0이면 pop()
3. 입력이 모두 끝난 후 sum(list) 출력
'''

K = int(input())
nums = []
for i in range(K):
    num = int(input())
    
    # 입력 값이 0이 아니면 append
    if num != 0:
        nums.append(num)
    else:
        nums.pop()

print(sum(nums))