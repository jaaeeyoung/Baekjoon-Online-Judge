'''
===================================================================================================================================
문제
===================================================================================================================================
[1541] 잃어버린 괄호
===================================================================================================================================
Log
===================================================================================================================================
' 2022-03-04-FRI : 문제 파악
                   문제 해결
===================================================================================================================================
'''
'''
1. 숫자는 숫자끼리, 연산자는 연산자끼리 각각 다른 List에 저장
    1.1. 숫자를 저장할 때 자릿수 생각해서 정수로 담기
2. A - B + C의 경우 - 연산자 뒤의 값 모두 계산하기
    2.1. - 연산자가 여러 개 있는 경우 A - B + C - D에서 A - (B+C) - D 로 계산
'''

# 입력
data = input()

operator_ = []
nums = []
temp = []
index = 0
for i in range(len(data)):
    if data[i] in ['+', '-']:
        operator_.append(data[i])
        # 숫자 자릿수에 맞춰서 하나의 숫자로 만들기
        nums.append(0)
        for j in range(len(temp)):
            nums[index] += temp[-1] * (10**j)
            del temp[-1]
        index += 1
    else:
        temp.append(int(data[i]))
# 마지막 숫자 추가
nums.append(0)
for j in range(len(temp)):
    nums[index] += temp[-1] * (10**j)
    del temp[-1]

# - 연산자 나오면 그 다음 - 연산자 전까지 + 모두 계산
i = 0
while True:

    # operator가 비어있으면 while문 돌지 않고 바로 출력
    if not operator_:
        break
    
    # - 연산자가 있으면 -연산자와 -연산자 사이의 값 모두 계산
    if operator_[i] == '-':
        
        index = 0
        flag = False # - 연산자 못찾으면 True
        
        if len(operator_) == 1 or i == len(operator_)-1:
            flag = True
            
        # 다음 - 연산자 찾기
        for j in range(i+2, len(operator_)+1):
            if operator_[j-1] == '-':
                index = j-1
                flag = False
                break
            else:
                flag = True
        
        # 그 뒤에 - 연산자가 없었다면
        if flag == True:
            nums[i+1] = sum(nums[i+1:])
            index = len(nums) - 1
        else: # - 연산자 있으면
            nums[i+1] = sum(nums[i+1:index+1])
        
        # 다음 - 연산자 전까지 모두 계산
        if '+' in  operator_[i+1:index]:
            temp = i + 2
            end = index + 1
            while True:
                nums[i + 2] = 0
                del operator_[i + 1]
                if nums[i + 2] == 0:
                    del nums[i + 2]
                    end -= 1
            
                if i + 2 == end:
                    break

    if i == len(operator_) - 1:
        break
    
    i += 1
    
for i in range(len(operator_)):
    if operator_[i] == '-':
        index = operator_.index('-')
        nums[index] -= nums[index+1]
        del nums[index+1]
print(sum(nums))