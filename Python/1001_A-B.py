'''
===================================================================================================================================
문제
===================================================================================================================================
[1001] A-B
===================================================================================================================================
시간 및 메모리 제한
===================================================================================================================================
# 시간 제한 : 2 초
# 메모리 제한 : 128 MB
===================================================================================================================================
문제 설명
===================================================================================================================================
# 두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.
===================================================================================================================================
입력
===================================================================================================================================
# 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
===================================================================================================================================
출력
===================================================================================================================================
# 첫째 줄에 A-B를 출력한다.
===================================================================================================================================
입출력 예
===================================================================================================================================
input   output
3 2     1
===================================================================================================================================
입출력 예 설명
===================================================================================================================================
' 입출력 예 #1
    
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

A, B = map(int, input().split())
print(A-B)