/*
===================================================================================================================================
문제
===================================================================================================================================
[2739] 구구단 
===================================================================================================================================
시간 및 메모리 제한
===================================================================================================================================
# 시간 제한 : 1 초
# 메모리 제한 : 128 MB
===================================================================================================================================
문제 설명
===================================================================================================================================
# N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.
===================================================================================================================================
입력
===================================================================================================================================
# 첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 9보다 작거나 같다.
===================================================================================================================================
출력
===================================================================================================================================
# 출력형식과 같게 N*1부터 N*9까지 출력한다.
===================================================================================================================================
입출력 예
===================================================================================================================================
입력
2

출력
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18

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
*/

#include <stdio.h>
int main(void)
{
    int N,a=1;
    scanf("%d",&N);
    for(int i=1;i<=9;i++)
    {
        printf("%d * %d = %d\n",N,a,N*a);
        a++;
    }
}