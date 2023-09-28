"""
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	19573	7179	5257	42.712%
문제
n(1 ≤ n ≤ 100)개의 도시가 있다. 그리고 한 도시에서 출발하여
다른 도시에 도착하는 m(1 ≤ m ≤ 100,000)개의 버스가 있다.
각 버스는 한 번 사용할 때 필요한 비용이 있다.

모든 도시의 쌍 (A, B)에 대해서 도시 A에서 B로 가는데
필요한 비용의 최솟값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 도시의 개수 n이 주어지고 둘째 줄에는 버스의 개수 m이 주어진다.
그리고 셋째 줄부터 m+2줄까지 다음과 같은 버스의 정보가 주어진다.
먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다.
버스의 정보는 버스의 시작 도시 a, 도착 도시 b, 한 번 타는데 필요한 비용 c로 이루어져 있다.
시작 도시와 도착 도시가 같은 경우는 없다. 비용은 100,000보다 작거나 같은 자연수이다.

시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.

출력
n개의 줄을 출력해야 한다. i번째 줄에 출력하는 j번째 숫자는 도시 i에서 j로 가는데 필요한 최소 비용이다.
만약, i에서 j로 갈 수 없는 경우에는 그 자리에 0을 출력한다.
"""
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
inf = sys.maxsize

dp = [[inf]*n for _ in range (n)]
for i in range(m):
    a,b,c = map(int,input().split())
    if dp[a-1][b-1] > c:
        dp[a-1][b-1] = c
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i!=j and dp[i][j] > dp[i][k] + dp[k][j]:
                dp[i][j] = dp[i][k] + dp[k][j]

for i in range(n):
    for j in range(n):
        if dp[i][j]==inf:
            dp[i][j]=0

for i in dp:
    print(*i)


#다익스트라 알고리즘으로 구현
#정답이긴하나, 시간이 오래걸려 플로이드 와샬로 구현
"""
import sys
from collections import deque
input = sys.stdin.readline
def bf(start):
    dp = [inf] * (n + 1)
    dp[start] = 0
    queue = deque()
    queue.append( [start,0] )
    while queue:
        a,b = queue.popleft()
        for go,wei in s[a]:
            if dp[go] > b+wei:
                dp[go] = b+wei
                queue.append([go,b+wei])
    for i in range (n+1):
        if dp[i] == inf:
            dp[i]=0
    return dp

inf = sys.maxsize
n = int(input())
edge = int(input())

s = [[] for _ in range(n + 1)]

for i in range(edge):
    u, v, w = map(int, sys.stdin.readline().split())
    s[u].append([v, w])

for i in range (1,n+1):
    print(*bf(i)[1:])
"""