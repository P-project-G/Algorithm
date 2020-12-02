"""
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	24223	2355	1469	16.667%
문제
N개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 버스가 M개 있다.
각 버스는 A, B, C로 나타낼 수 있는데, A는 시작도시, B는 도착도시,
C는 버스를 타고 이동하는데 걸리는 시간이다. 시간 C가 양수가 아닌 경우가 있다.
C = 0인 경우는 순간 이동을 하는 경우, C < 0인 경우는 타임머신으로 시간을 되돌아가는 경우이다.

1번 도시에서 출발해서 나머지 도시로 가는 가장 빠른 시간을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 도시의 개수 N (1 ≤ N ≤ 500), 버스 노선의 개수 M (1 ≤ M ≤ 6,000)이 주어진다.
둘째 줄부터 M개의 줄에는 버스 노선의 정보 A, B, C (1 ≤ A, B ≤ N, -10,000 ≤ C ≤ 10,000)가 주어진다.

출력
만약 1번 도시에서 출발해 어떤 도시로 가는 과정에서 시간을 무한히 오래 전으로 되돌릴 수 있다면
첫째 줄에 -1을 출력한다. 그렇지 않다면 N-1개 줄에 걸쳐 각 줄에 1번 도시에서 출발해
2번 도시, 3번 도시, ..., N번 도시로 가는 가장 빠른 시간을 순서대로 출력한다.
만약 해당 도시로 가는 경로가 없다면 대신 -1을 출력한다.
# 벨만포드 알고리즘 사용
"""
import sys

def bf(start):
    dp[start] = 0
    for cnt in range(n+1):
        for a in range(n+1):
            if dp[a] != inf:
                for b,c in s[a]:
                    if dp[b] > dp[a]+c:
                        dp[b] = dp[a]+c
                        if cnt == n:
                            print(-1)
                            return
    for i in dp[2:]:
        print(i if i != inf else "-1")
    return

inf = sys.maxsize
n, edge = map(int, sys.stdin.readline().split())
s = [[] for _ in range(n + 1)]
dp = [inf] * (n + 1)

for i in range(edge):
    u, v, w = map(int, sys.stdin.readline().split())
    s[u].append([v, w])

bf(1)