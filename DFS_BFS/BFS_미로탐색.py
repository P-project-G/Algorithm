"""
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	192 MB	78159	29826	18967	36.953%

문제
N×M크기의 배열로 표현되는 미로가 있다.

1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다.
이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는
최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때,
서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다.
칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

입력
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다.
다음 N개의 줄에는 M개의 정수로 미로가 주어진다.
각각의 수들은 붙어서 입력으로 주어진다.

출력
첫째 줄에 지나야 하는 최소의 칸 수를 출력한다.
항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.
"""
from collections import deque
n,m=map(int,input().split())
maze=[list(map(int,input())) for _ in range (n)]
vertical=[1,-1,0,0]
horizon=[0,0,1,-1]
visit = [[0] * m for _ in range(n)]
queue=deque()
queue.append((0,0))
while queue:
    x,y = queue.popleft()
    for i in range(4):
        dx=x+vertical[i]
        dy=y+horizon[i]
        if n>dx>=0 and m>dy>=0 and maze[dx][dy]==1:
            maze[dx][dy]=maze[x][y]+1
            queue.append((dx,dy))
print(maze[n-1][m-1])

"""
백트래킹느낌 실패
def dfs(i,j,cnt):
    global mcnt
    if i==n-1 and j==m-1 and cnt<mcnt:
        mcnt=cnt

    if maze[i][j]==1:
        for k in range(4):
            v=i+vertical[k]
            h=j+horizon[k]
            if v<0 or h<0 or v>n-1 or h>m-1:
                continue
            if maze[v][h]==1 and visit[v][h]==0:
                visit[v][h]=1
                dfs(v,h,cnt+1)
                visit[v][h]=0


n,m=map(int,input().split())
maze=[list(map(int,input())) for _ in range (n)]
vertical=[1,-1,0,0]
horizon=[0,0,1,-1]
mcnt=10000
answer=[]
visit = [[0] * m for _ in range(n)]
dfs(0,0,1)
print(mcnt)
"""