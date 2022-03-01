'''
===================================================================================================================================
문제
===================================================================================================================================
[1934] 최소공배수
===================================================================================================================================
시간 및 메모리 제한
===================================================================================================================================
# 시간 제한 : 1 초
# 메모리 제한 : 128 MB
===================================================================================================================================
문제 설명
===================================================================================================================================
# 두 자연수 A와 B에 대해서, A의 배수이면서 B의 배수인 자연수를 A와 B의 공배수라고 한다. 이런 공배수 중에서 가장 작은 수를 최소공배수라고 
  한다. 예를 들어, 6과 15의 공배수는 30, 60, 90등이 있으며, 최소 공배수는 30이다.

두 자연수 A와 B가 주어졌을 때, A와 B의 최소공배수를 구하는 프로그램을 작성하시오.
===================================================================================================================================
입력
===================================================================================================================================
# 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 둘째 줄부터 T개의 줄에 걸쳐서 A와 B가 주어진다. (1 ≤ A, B ≤ 45,000)
===================================================================================================================================
출력
===================================================================================================================================
# 첫째 줄부터 T개의 줄에 A와 B의 최소공배수를 입력받은 순서대로 한 줄에 하나씩 출력한다.
===================================================================================================================================
입출력 예
===================================================================================================================================
입력 1
3
1 45000
6 10
13 17

출력 1
45000
30
221
===================================================================================================================================
알고리즘 분류
===================================================================================================================================
# 수학
# 정수론
# 유클리드 호제법
===================================================================================================================================
Log
===================================================================================================================================
' 2022-02-19 SAT : 문제 파악
                   틀림 - 어느 부분이 틀렸는지 모르겠음
                   [11653] 소인수분해와 동일한 알고리즘을 사용했기 때문에 인수분해 이후 최소공배수 구하는 과정에서 잘못된 것 같음
                   틀린 건 고쳤지만 시간 초과 -> 유클리드 호제법 사용해봐야할듯
' 2022-03-01 TUE : 유클리드 호제법 적용
                   문제 해결
===================================================================================================================================
'''

'''
Algorithm
1. 두 숫자를 각각 인수분해 해서 각자의 Dictionary에 인수 별 몇 개씩 필요한지 저장
2. A와 B의 각 인수의 최솟값을 구하고 모든 인수 곱해서 최소 공배수 출력
'''

# 유클리드 호제법
# A와 B의 최대 공약수 = B와 A%B의 최대 공약수
def euclid(num1, num2):
    A = max(num1, num2)
    B = min(num1, num2)
    R = A % B
    # A와 B가 나누어 떨어지면 B RETURN
    if R == 0:
        return B
    else: # 나누어 떨어지지 않으면 재귀
        return euclid(B, R)
    
T = int(input())
answer = []
for i in range(T):
    A, B = map(int, input().split())
    
    # A와 B가 서로 배수관계라면 둘 중 큰 수 출력
    if A % B == 0 or B % A == 0:
        print(max(A, B))
        continue
    
    # 배수관계가 아니라면 EUCLID 호제법 이용
    # 최소공배수 = A*B//최대공약수
    print((A * B)//euclid(A, B))