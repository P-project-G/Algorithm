"""
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	51038	32499	21573	61.664%
문제
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다.
합을 나타낼 때는 수를 1개 이상 사용해야 한다.

1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
1+3
3+1
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로
나타내는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고,
정수 n이 주어진다. n은 양수이며 11보다 작다.

출력
각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.

"""
def dfs(value, n):
    global cnt
    if value == n:
        cnt += 1

    elif value > n:
        pass

    else:
        dfs(value+1,n)
        dfs(value+2,n)
        dfs(value+3,n)
T=int(input())
n = list(int(input()) for i in range (T))

for i in range (T):
    cnt=0
    dfs(0,n[i])
    print(cnt)