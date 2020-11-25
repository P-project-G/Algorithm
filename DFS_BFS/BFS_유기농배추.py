from collections import deque
def bfs(i,j):
    queue=deque()
    queue.append((i,j))
    visit[i][j]=1
    while queue:
        nx,ny=queue.popleft()
        for k in range(4):
            kx=nx+dx[k]
            ky=ny+dy[k]
            if kx < 0 or ky < 0 or kx > row - 1 or ky > col - 1:
                continue
            if visit[kx][ky]==0 and farm[kx][ky]==1:
                queue.append((kx,ky))
                visit[kx][ky] = 1

t=int(input()) # 테스트케이스
dx,dy=[1,-1,0,0],[0,0,1,-1]
for _ in range (t):
    k=0
    row, col, cnt = map(int, input().split())
    farm = [[0]*col for i in range (row)]

    for _ in range (cnt):
        x,y=map(int,input().split())
        farm[x][y]=1

    visit = [[0]*col for i in range (row)]

    for i in range (row):
        for j in range (col):
            if visit[i][j]==0 and farm[i][j]==1:
                bfs(i,j)
                k+=1

    print(k)

