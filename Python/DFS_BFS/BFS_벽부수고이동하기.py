"""
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	192 MB	44080	10498	6507	22.690%
문제
N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고,
1은 이동할 수 없는 벽이 있는 곳을 나타낸다.
당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데,
이때 최단 경로로 이동하려 한다. 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데,
이때 시작하는 칸과 끝나는 칸도 포함해서 센다.

만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면,
벽을 한 개 까지 부수고 이동하여도 된다.

맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다.
다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.

출력
첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.


"""
from collections import deque
import sys
input=sys.stdin.readline


def bfs():
    queue = deque()
    queue.append((0,0,1))
    visit = [[ [0] * 2 for _ in range (m) ] for _ in range (n) ]
    visit[0][0][1] = 1
    while queue:
        a,b,c = queue.popleft()
        if a == n-1 and b == m-1 :
            for i in visit:
                print(i)
            print()
            return visit[a][b][c]

        for k in range (4):
            x=a+v[k]
            y=b+h[k]
            if n>x>=0 and m>y>=0:
                if graph[x][y] == 1 and c == 1:
                    visit[x][y][0] = visit[a][b][1] + 1
                    queue.append((x,y,0))
                elif graph[x][y] == 0 and visit[x][y][c]==0:
                    visit[x][y][c] = visit[a][b][c] + 1
                    queue.append((x,y,c))
    return -1


n,m = map(int,input().split())
graph= [ list(map(int, input().strip())) for _ in range (n)]

v=[1,-1,0,0]
h=[0,0,1,-1]
print(bfs())




# for문으로 인한 시간초과
"""
def bfs(i,j,d):
    queue=deque()
    queue.append((i,j,d))

    while queue:
        a,b,c = queue.popleft()
        if a==n-1 and b==m-1:
            answer.append(c)

        for k in range (4):
            dx = a+v[k]
            dy = b+h[k]
            if n>dx>=0 and m>dy>=0 and visit[dx][dy]==0 and graph[dx][dy]==0:
                visit[dx][dy]=1
                queue.append((dx,dy,c+1))


n,m=map(int,input().split())
graph=[list(map(int,input().strip())) for _ in range (n)]
visit=[[0]*m for _ in range (n)]
v = [1,-1,0,0]
h = [0,0,1,-1]
answer=[]

bfs(0,0,0)
for i in range (n):
    for j in range (m):
        if graph[i][j]==1:
            visit = [[0] * m for _ in range(n)]
            graph[i][j]=0
            bfs(0,0,0)
            graph[i][j]=1

if not answer:
    print(-1)
else:
    print(min(answer)+1)
"""