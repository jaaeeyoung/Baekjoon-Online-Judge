'''
===================================================================================================================================
문제
===================================================================================================================================
[4375] 1
===================================================================================================================================
Log
===================================================================================================================================
' 2022-03-12-SAT : 문제 파악
                   문제 해결
===================================================================================================================================
'''

while True: 
    try: 
        n = int(input()) 
        num = 1 
        
        while True: 
            if int('1'*num) % n == 0: 
                print(len('1'*num)) 
                break 
            num += 1 
    except: 
        break