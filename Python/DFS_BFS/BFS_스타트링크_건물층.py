from collections import deque
import sys
input = sys.stdin.readline

def bfs(i):
    queue = deque()
    queue.append(i)
    visit = [0] * F
    visit[i] = 1

    while queue:
        s = queue.popleft()
        for k in range (2):
            search_s = s + search[k]
            if search_s < 0 or search_s > F-1:
                continue
            if visit[search_s] == 0:
                queue.append(search_s)
                dp[search_s] = dp[s] + 1
                visit[search_s] = 1




#F S G U D
#F = 건물의 층
#S = 현재있는 위치
#G = 스타트링크가 있는 위치
#U = 올라가는 층 수
#D = 내려가는 층 수
F,S,G,U,D = map(int,input().split())
search = [U,-D]
dp = [-1] * F
dp[S-1] = 0
bfs(S-1)
if dp[G-1] != -1:
    print(dp[G-1])
else:
    print('use the stairs')