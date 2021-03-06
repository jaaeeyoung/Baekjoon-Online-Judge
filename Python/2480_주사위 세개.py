'''
===================================================================================================================================
문제
===================================================================================================================================
[2480] 주사위 세개
===================================================================================================================================
Log
===================================================================================================================================
' 2022-03-02-WED : 문제 파악
                   문제 해결 
===================================================================================================================================
'''
'''
1. 입력 값을 Dictionary에 추가 (개수 count)
2. for문을 돌면서 value가 3이면 10000 + key * 100
3. value가 2이면 1000 + key * 100
4. 그 외의 상황이면 max(key) * 100
'''

# 입력
data = list(map(int, input().split()))

# 입력 값 Dictionary에 저장 (key: 입력 값, value: 횟수)
dict_ = {}
for i in data:
    if i not in dict_:
        dict_[i] = 1
    else:
        dict_[i] += 1

flag = False # 같은 숫자가 있는 경우 False, 모두 다른 경우 True
for key, value in dict_.items():
    if value == 3:
        print(10000 + key * 1000)
        flag = False
        break
    elif value == 2:
        print(1000 + key * 100)
        flag = False
        break
    else:
        flag = True
        
if flag:
    print(max(dict_.keys()) * 100)