'''
===================================================================================================================================
문제
===================================================================================================================================
[2869] 달팽이는 올라라고 싶다
===================================================================================================================================
Log
===================================================================================================================================
' 2022-03-02-WED : 문제 파악
                   알고리즘을 다시 생각해볼것 ㅠㅠ
===================================================================================================================================
'''
'''
1. 정상 높이가 A에 의해 나누어 떨어지면 마지막에 올라가기만 하고 내려오지 않아도 되므로 V - B
2. 나누어 떨어지지 않으면 V//(A - B) + 1
'''

A, B, V = map(int, input().split())
if V % A != 0:
    if V % (A - B) == 0:
        print(V // (A - B) - 1)
    else:
        print(V // (A - B) + 1)
else:
    # if V % A == 0:
    print(V - B)