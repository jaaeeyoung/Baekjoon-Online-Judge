'''
===================================================================================================================================
문제
===================================================================================================================================
[5566] 주사위 게임
===================================================================================================================================
시간 및 메모리 제한
===================================================================================================================================
# 시간 제한 : 1 초
# 메모리 제한 : 128 MB
===================================================================================================================================
문제 설명
===================================================================================================================================
# 상근이는 혼자 보드 게임을 하고 있다. 이 보드 게임의 보드는 N칸으로 이루어져 있고, 출발점은 1칸, 도착점은 N칸이다. 각 칸에는 지시 사항이
  적혀있다. 지시 사항은 말을 얼만큼 이동해야 하는지가 쓰여 있다. 

# 상근이는 도착점에 도착할 때까지 주사위를 굴려 나온 눈의 수만큼 그 칸으로 이동한다. 이때, 도착한 칸에 쓰여 있는 지시만큼 말을 다시 이동
  시킨다. 지시 사항으로 이동해서 도착한 칸에 쓰여 있는 지시는 따르지 않는다.

# N칸에 도착했을 때와 그 칸을 넘는 경우도 도착한 것이다.

# 상근이가 던졌을 때 나온 주사위의 눈과 보드판의 지시사항이 주어졌을 때, 몇 번 만에 도착하는지 구하는 프로그램을 작성하시오.
===================================================================================================================================
입력
===================================================================================================================================
# 첫째 줄에 N과 M이 주어진다. M은 상근이가 주사위를 던진 횟수이다. (2 ≤ N ≤ 1000, 1 ≤ M ≤ 1000)

# 다음 N개 줄에는 -999이상 999이하의 정수가 하나씩 적혀있다. i번째 정수는 i번 칸에 쓰여 있는 지시사항 X이다. 이때, X가 0이면 아무것도 하
  지 않고 그 자리에 멈춰 있는다. X가 양수인 경우에는 X칸 더 앞으로 진행하는 것을, 음수인 경우에는 |X|칸 뒤로 진행하는 것을 나타낸다.

# 다음 M개 줄에는 1이상 6이하의 정수가 주어진다. j번째 정수는 상근이가 주사위를 j번째로 던졌을 때, 나온 눈이다.

# 1번 칸과 N번 칸에 쓰여 있는 지시사항은 항상 0이다. 또, 항상 주사위를 M번 이하로 던져서 도착할 수 있다.  또, 1보다 작은 칸으로 이동하라
  는 지시가 있는 경우도 없다.
===================================================================================================================================
출력
===================================================================================================================================
# 주사위를 몇 번 던져서 도착할 수 있는지 출력한다.
===================================================================================================================================
입출력 예
===================================================================================================================================
입력 1
10 5
0
0
5
6
-3
8
1
8
-4
0
1
3
5
1
5

출력 1
5

입력 2
10 10
0
-1
-1
4
4
-5
0
1
-6
0
1
5
2
4
6
5
5
4
1
6

출력 2
6
===================================================================================================================================
알고리즘 분류
===================================================================================================================================
# 구현
# 시뮬레이션
===================================================================================================================================
Log
===================================================================================================================================
' 2022-02-19-SAT : 문제 파악
                   문제 해결
===================================================================================================================================
'''

'''
Algorithm
1. N번 for문 돌려 N개의 정수 리스트에 저장
2. M번 for문 돌려 M개의 정수 리스트에 저장
3. M이 담긴 리스트 하나씩 돌면서 해당하는 숫자만큼 location 이동
-> 한 번 돌때마다 count 증가
4. 이동한 곳의 숫자에 따라 location 추가 이동
5. location이 N보다 크거나 같으면 break후 count 출력
'''

N, M = map(int, input().split())
direction = []
for _ in range(N):
  direction.append(int(input()))
  
dice = []
for _ in range(M):
  dice.append(int(input()))

location = 1
count = 0
for i in dice:
  location += i
  count += 1
  
  if location >= N: # 현재 위치가 마지막 칸이거나 넘어가면
    break # break
  
  if direction[location - 1] != 0: # direction에 쓰여있는 수가 0이 아니면
    location += direction[location - 1]
    
  if location >= N: # 현재 위치가 마지막 칸이거나 넘어가면
    break # break
  
print(count)