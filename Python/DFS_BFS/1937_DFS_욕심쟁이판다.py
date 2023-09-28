from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(v,h):
    if dp[v][h]:
        return dp[v][h]
    dp[v][h] = 1

    for k in range(4):
        dv = v + vertical[k]
        dh = h + horizon[k]
        if dv<0 or dh<0 or dv>n-1 or dh>n-1:
            continue

        if forest[v][h] < forest[dv][dh]:
            dp[v][h] = max(dp[v][h],dfs(dv,dh)+1)

    return dp[v][h]


vertical = [1,-1,0,0]
horizon = [0,0,1,-1]

iMax = 0

n = int(input())
forest = [list(map(int,input().split())) for _ in range (n)]
dp = [ [0]*n for _ in range (n) ]
for i in range (n):
    for j in range (n):
        iMax = max(iMax,dfs(i,j))


print(iMax)

"""

시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	256 MB	25192	8046	5225	29.864%

문제
n*n의 크기의 대나무 숲이 있다. 욕심쟁이 판다는 어떤 지역에서 대나무를 먹기 시작한다. 그리고 그 곳의 대나무를 다 먹어 치우면 상, 하, 좌, 우 중 한 곳으로 이동을 한다. 그리고 또 그곳에서 대나무를 먹는다. 그런데 단 조건이 있다. 이 판다는 매우 욕심이 많아서 대나무를 먹고 자리를 옮기면 그 옮긴 지역에 그 전 지역보다 대나무가 많이 있어야 한다. 만약에 그런 지점이 없으면 이 판다는 불만을 가지고 단식 투쟁을 하다가 죽게 된다(-_-)

이 판다의 사육사는 이런 판다를 대나무 숲에 풀어 놓아야 하는데, 어떤 지점에 처음에 풀어 놓아야 하고, 어떤 곳으로 이동을 시켜야 둘 다 소중한 생명이지만 판다가 최대한 오래 살 수 있는지 고민에 빠져 있다. 우리의 임무는 이 사육사를 도와주는 것이다. n*n 크기의 대나무 숲이 주어져 있을 때, 이 판다가 최대한 오래 살려면 어떤 경로를 통하여 움직여야 하는지 구하여라.

입력
첫째 줄에 대나무 숲의 크기 n(1 ≤ n ≤ 500)이 주어진다. 그리고 둘째 줄부터 n+1번째 줄까지 대나무 숲의 정보가 주어진다. 대나무 숲의 정보는 공백을 사이로 두고 각 지역의 대나무의 양이 정수 값으로 주어진다. 대나무의 양은 1,000,000보다 작거나 같은 자연수이다.

출력
첫째 줄에는 판다가 최대한 살 수 있는 일수(K)를 출력한다.

예제 입력 1 
4
14 9 12 10
1 11 5 4
7 15 2 13
6 3 16 8

예제 출력 1 
4
"""


"""
bfs로 구현해봤는데 시간초과

def bfs(i,j):
    if dp[i][j] == 0:
        dp[i][j] = 1

    queue = deque()
    queue.append([i,j,1])

    while queue:
        ver,hor,cnt = queue.popleft()
        for k in range (4):
            dv = ver + vertical[k]
            dh = hor + horizon[k]
            if dv<0 or dh<0 or dv>n-1 or dh>n-1:
                continue

            if forest[ver][hor] < forest[dv][dh]:
                dp[i][j] = max(dp[i][j],cnt+1)
                queue.append([dv, dh, cnt+1])
    return dp[i][j]
"""