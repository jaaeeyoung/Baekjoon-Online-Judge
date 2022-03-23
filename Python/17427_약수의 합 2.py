'''
===================================================================================================================================
문제
===================================================================================================================================
[17427] 약수의 합 2
===================================================================================================================================
Log
===================================================================================================================================
' 2022-03-23-WED : 문제 파악
                   시간 초과
                   문제 해결
===================================================================================================================================
'''
'''
Algorithm
N까지의 약수 중 i라는 숫자는 N//i개 존재
-> i가 1부터 N까지 증가하면서 i의 개수 * i 더하기
'''
N = int(input())
sum_ = 0
for i in range(1, N+1):
    sum_ += i * (N//i)
print(sum_)