import sys
from collections import deque
input = sys.stdin.readline

#bfs, 메모리초과
def bfs(start):
    queue=deque()
    queue.append( [start,0,0] )
    mv=[inf,inf]
    while queue:
        x,y,z = queue.popleft()
        if x==n:
            if y<=mv[0] and z<mv[1]:
                mv=[y,z]

        for arrive, prices, time in s[x]:
            t_time = time + z
            total_prices = prices + y

            if total_prices>m:
                continue

            queue.append( (arrive,total_prices,t_time) )
    if mv[1] == inf:
        return 'Poor KCM'
    return mv[1]

inf = sys.maxsize
t=int(input())
for _ in range (t):
    n,m,k = map(int,input().split())
    s=[[] for i in range (n+1)]
    for _ in range (k):
        u,v,c,d = map(int,input().split())
        s[u].append( [v,c,d] )
    print(bfs(1))
