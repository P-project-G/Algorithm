"""
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	4457	1695	1345	40.185%

문제
n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열이 있다. ai의 값은 1보다 크거나 같고, 1000000보다 작거나 같은 자연수이다. 자연수 x가 주어졌을 때, ai + aj = x (1 ≤ i < j ≤ n)을 만족하는 (ai, aj)쌍의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수열의 크기 n이 주어진다. 다음 줄에는 수열에 포함되는 수가 주어진다. 셋째 줄에는 x가 주어진다. (1 ≤ n ≤ 100000, 1 ≤ x ≤ 2000000)

출력
문제의 조건을 만족하는 쌍의 개수를 출력한다.

예제 입력 1
9
5 12 7 10 9 1 2 3 11
13

예제 출력 1
3

"""
# 투포인터 사용 (확실히 빠르고 메모리가 적다)
import sys
input = sys.stdin.readline

n = int(input()) # 수열의 크기 n
numarr = list(map(int,input().split())) # 수열
x = int(input()) # 자연수 x
numarr = sorted(numarr)

start,end = 0,n-1
count = 0

while start<end:

    s,e = numarr[start],numarr[end]
    if numarr[start]+numarr[end] == x:
        count += 1
        start += 1
        end -= 1

    elif s+e > x:
        end -= 1

    else:
        start += 1

print(count)


# 메모리초과
"""
from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input()) # 수열의 크기 n
numarr = list(map(int,input().split())) # 수열
x = int(input()) # 자연수 x
numarr = filter(lambda k:k[0]+k[1]==x,combinations(numarr,2))
print(len(list(numarr)))
"""