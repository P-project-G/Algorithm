import sys
from collections import deque
input = sys.stdin.readline

def dijkstra(start,street):
    dp = [sys.maxsize]*(N+1)
    dp[start] = 0
    queue = deque()
    queue.append([0,start])
    while queue:
        ti,idx = queue.popleft()
        for time,arrive in street[idx]:
            if dp[arrive] > ti+time:
                dp[arrive] = ti+time
                queue.append([ti+time,arrive])
    return dp

N,M,X = map(int,input().split())
street = [ [] for _ in range (N+1) ]
r_street = [ [] for _ in range (N+1) ]
for i in range (M):
    s,e,t = map(int,input().split())
    street[s].append([t,e])
    r_street[e].append([t,s])

idx_result = dijkstra(X,street)
X_result = dijkstra(X,r_street)

mx = 0
for i in range (1,N+1):
    total = idx_result[i]+X_result[i]
    if mx < total:
        mx = total
print(mx)