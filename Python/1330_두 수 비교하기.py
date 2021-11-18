'''
===================================================================================================================================
문제
===================================================================================================================================
[1316] 그룹 단어 체커
===================================================================================================================================
시간 및 메모리 제한
===================================================================================================================================
# 시간 제한 : 1 초
# 메모리 제한 : 512 MB
===================================================================================================================================
문제 설명
===================================================================================================================================
# 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.
===================================================================================================================================
입력
===================================================================================================================================
# 첫째 줄에 A와 B가 주어진다. A와 B는 공백 한 칸으로 구분되어져 있다.
===================================================================================================================================
출력
===================================================================================================================================
# 첫째 줄에 다음 세 가지 중 하나를 출력한다.

    A가 B보다 큰 경우에는 '>'를 출력한다.
    A가 B보다 작은 경우에는 '<'를 출력한다.
    A와 B가 같은 경우에는 '=='를 출력한다.
===================================================================================================================================
제한
===================================================================================================================================
-10,000 ≤ A, B ≤ 10,000
===================================================================================================================================
입출력 예
===================================================================================================================================
입력    출력
1 2     <
10 2    >
5 5     ==
===================================================================================================================================
알고리즘 분류
===================================================================================================================================
# 수학
# 구현
# 사칙연산
===================================================================================================================================
Log
===================================================================================================================================

===================================================================================================================================
'''

A, B = input().split()

if int(A) > int(B):
    print('>')
elif int(A) < int(B):
    print('<')
else:
    print('==')