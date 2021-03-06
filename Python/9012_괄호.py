'''
===================================================================================================================================
문제
===================================================================================================================================
[9012] 괄호
===================================================================================================================================
Log
===================================================================================================================================
' 2022-03-19-SAT : 문제 파악
                   문제 해결
===================================================================================================================================
'''

'''
1. ( 모양인 경우 리스트에 해당 문자 append
2. ) 모양인 경우 리스트에서 pop
2.1. pop이 불가능하면, 마지막에 리스트에 뭔가 남아있으면 NO 반환
2.2. 마지막에 리스트에 아무것도 없으면 YES 반환
'''

T = int(input())
for _ in range(T):
    string_ = list(input())
    
    list_ = []
    flag = False
    for chr in string_:
        # ( 모양인 경우 리스트에 해당 문자 append
        if chr == '(':
            list_.append(chr)
        else: # ) 모양인 경우 리스트에서 pop
            if len(list_) == 0: # 리스트에서 pop이 불가능한 경우 
                flag = True
                break
            list_.pop()
    
    # 마지막에 리스트에 뭔가 남아있으면 NO 반환
    if flag or len(list_) > 0:
        print('NO')
    else:
        print('YES')