from collections import deque
import sys
input = sys.stdin.readline


def bfs(start):
    visit = [False]*(n+1)
    queue=deque()
    queue.append(start)
    visit[start]=True

    while queue:
        cur = queue.popleft()
        for i in s[cur]:
            if visit[i] == False:
                visit[i] = True
                parent[i] = cur
                queue.append(i)
n=int(input())
parent=[ [] for _ in range (n+1) ]
s=[ [] for _ in range (n+1) ]
for i in range (n-1):
    a,b=map(int,input().split())
    s[b].append(a)
    s[a].append(b)
answer=[]
bfs(1)
for i in range (2,n+1):
    print(parent[i])