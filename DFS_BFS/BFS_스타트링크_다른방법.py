from collections import deque
import sys
input = sys.stdin.readline


def bfs(i):
    queue = deque()
    queue.append([i,1])
    dp = [inf]*(F+1)
    dp[i] = 0
    while queue:
        s,d = queue.popleft()
        if s <= F-U:
            if d < dp[s+U]:
                if dp[s+U] == inf:
                    dp[s+U] = d
                    queue.append([s+U,d+1])
        if s > D:
            if d < dp[s-D]:
                if dp[s-D] == inf:
                    dp[s-D] = d
                    queue.append([s-D,d+1])

    if dp[G] == inf:
        print("use the stairs")
    else:
        print(dp[G])

#F S G U D
#F = 건물의 층
#S = 현재있는 위치
#G = 스타트링크가 있는 위치
#U = 올라가는 층 수
#D = 내려가는 층 수
F,S,G,U,D = map(int,input().split())
inf = sys.maxsize
bfs(S)
