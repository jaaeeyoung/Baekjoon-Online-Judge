'''
===================================================================================================================================
문제
===================================================================================================================================
[1157] 단어 공부
===================================================================================================================================
시간 및 메모리 제한
===================================================================================================================================
# 시간 제한 : 2 초
# 메모리 제한 : 128 MB
===================================================================================================================================
문제 설명
===================================================================================================================================
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자
  를 구분하지 않는다.
===================================================================================================================================
입력
===================================================================================================================================
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
===================================================================================================================================
출력
===================================================================================================================================
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
===================================================================================================================================
입출력 예
===================================================================================================================================
input       output
Mississipi  ?
zZa         Z
z           Z
baaa        A
===================================================================================================================================
알고리즘 분류
===================================================================================================================================
# 구현
# 문자열
===================================================================================================================================
Log
===================================================================================================================================

===================================================================================================================================
'''

word = input()
word = word.upper()
list_ = [0 for _ in range(26)]
for i in word:
    list_[ord(i) - 65] += 1
max_ = max(list_)
count = 0
flag = 0
for i in list_:
    if i == max_:
        count += 1
        if count == 2:
            flag = 1
            print('?')
            break
if flag == 0:
    print(chr(list_.index(max_) + 65))