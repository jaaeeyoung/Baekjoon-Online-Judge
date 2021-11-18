/*
===================================================================================================================================
문제
===================================================================================================================================
[2439] 별 찍기-2
===================================================================================================================================
시간 및 메모리 제한
===================================================================================================================================
# 시간 제한 : 1 초
# 메모리 제한 : 128 MB
===================================================================================================================================
문제 설명
===================================================================================================================================
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.
===================================================================================================================================
입력
===================================================================================================================================
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
===================================================================================================================================
출력
===================================================================================================================================
# 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
===================================================================================================================================
입출력 예
===================================================================================================================================
입력
5

출력
    *
   **
  ***
 ****
*****
===================================================================================================================================
알고리즘 분류
===================================================================================================================================
# 구현
===================================================================================================================================
Log
===================================================================================================================================

===================================================================================================================================
*/

#include <stdio.h>
int main(void)
{
    int N;
    scanf("%d",&N);
    for(int i=0;i<N;i++)
    {
        for(int j=1;j<N-i;j++)
        {
            printf(" ");
        }
        for(int j=0;j<=i;j++)
        {
            printf("*");
        }
        printf("\n");
    }
}