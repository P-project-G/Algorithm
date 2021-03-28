def divided_conquest(a,b,c):
    if b==1:
        return a%c
    else:
        v = divided_conquest(a,b//2,c)
        if b%2 == 0:
            return v * v % c
        else:
            return v * v * a % c

a,b,c = map(int,input().split())
print(divided_conquest(a,b,c))

"""
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
0.5 초 (추가 시간 없음)	128 MB	35859	9132	6752	25.374%
문제
자연수 A를 B번 곱한 수를 알고 싶다. 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다. A, B, C는 모두 2,147,483,647 이하의 자연수이다.

출력
첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.

예제 입력 1 
10 11 12
예제 출력 1 
4
"""

"""
# pow 사용하면 더 간단
import sys
input = sys.stdin.readline

a,b,c = map(int,input().split()) # a,b,c <= 2,147,483,647 이하의 자연수
print(pow(a,b,c))
"""
