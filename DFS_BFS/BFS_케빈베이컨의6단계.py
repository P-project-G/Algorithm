from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    visit = [False]*(n+1)
    visit[start]=True
    queue=deque()
    queue.append([start,0])
    baken=[]
    while queue:
        a,cnt=queue.popleft()
        for i in s[a]:
            if visit[i]==False:
                visit[i]=True
                queue.append([i,cnt+1])
                baken.append(cnt+1)
    return sum(baken)

n,m = map(int,input().split())
s=[[] for _ in range (n+1)]

for _ in range (m):
    a,b=map(int,input().split())
    s[a].append(b)
    s[b].append(a)

answer=[]
for i in range (1,n+1):
    answer.append(bfs(i))
print(answer.index(min(answer))+1)