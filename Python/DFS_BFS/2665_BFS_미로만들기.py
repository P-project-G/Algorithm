from collections import deque
import sys
input = sys.stdin.readline

def bfs(i,j):
    queue = deque()
    queue.append([i,j,0])

    while queue:
        ver,hor,cnt = queue.popleft()
        for k in range (4):
            dv = ver+vertical[k]
            dh = hor+horizon[k]
            if dv<0 or dh<0 or dv>n-1 or dh>n-1:
                continue

            if maze[dv][dh] == '0':
                if dp[dv][dh] > cnt:
                    dp[dv][dh] = cnt+1
                    queue.append([dv,dh,cnt+1])
            if maze[dv][dh] == '1':
                if dp[dv][dh] > cnt:
                    dp[dv][dh] = cnt
                    queue.append([dv,dh,cnt])
    return dp[n-1][n-1]

vertical = [1,-1,0,0]
horizon = [0,0,1,-1]
n=int(input())
maze = [list(input().strip()) for _ in range (n)]
dp = [[2500]*n for _ in range (n)]
print(bfs(0,0))