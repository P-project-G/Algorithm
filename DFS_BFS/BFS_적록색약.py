from collections import deque
import sys

def bfs(i,j,color,rgb):
    visit[i][j]=1
    queue=deque()
    queue.append( (i,j) )
    while queue:
        v,h=queue.popleft()
        for k in range (4):
            dv = v + vertical[k]
            dh = h + horizon[k]
            if dv<0 or dh<0 or dv>n-1 or dh>n-1:
                continue

            if visit[dv][dh]==0 and rgb[dv][dh] == color:
                visit[dv][dh]=1
                queue.append( (dv,dh) )


vertical = [1,-1,0,0]
horizon = [0,0,1,-1]
n = int(input())
rgb = [ list(map(str,input())) for i in range (n) ]
visit = [ [0] * n for _ in range (n) ]

#적록색약 아닌 사람
rgb_cnt = 0
for i in range (n):
    for j in range (n):
        if visit[i][j]==0:
            bfs(i,j,rgb[i][j],rgb)
            rgb_cnt+=1

#적록색약인 사람
rg_cnt = 0
copy = [ [0]*n for _ in range (n) ]
visit = [ [0] * n for _ in range (n) ]

for i in range (n):
    for j in range (n):
        if rgb[i][j]=='G':
            copy[i][j]='R'
        else:
            copy[i][j]=rgb[i][j]

for i in range (n):
    for j in range (n):
        if visit[i][j]==0:
            bfs(i,j,copy[i][j],copy)
            rg_cnt+=1

print(rgb_cnt,rg_cnt)