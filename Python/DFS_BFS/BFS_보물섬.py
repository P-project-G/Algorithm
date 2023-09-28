from collections import deque
import sys
input = sys.stdin.readline

def bfs(i,j):
    queue = deque()
    queue.append([i,j])
    max_num = 0
    while queue:
        v,h = queue.popleft()
        for k in range (4):
            dv = v + vertical[k]
            dh = h + horizon[k]
            if dv<0 or dh<0 or dv>x-1 or dh>y-1:
                continue
            if treasure_map[dv][dh] != 'W' and visit[dv][dh]==0:
                visit[dv][dh]=1
                treasure_map[dv][dh] = treasure_map[v][h] + 1
                queue.append([dv,dh])
                max_num = max(max_num,treasure_map[dv][dh])
    return max_num

x,y=map(int,input().split())
treasure_map = [ list(input().strip()) for _ in range (x) ]

vertical = [1,-1,0,0]
horizon = [0,0,1,-1]

result=0
for i in range (x):
    for j in range (y):
        if treasure_map[i][j] != 'W':
            visit = [[0] * y for _ in range(x)]
            visit[i][j] = 1
            treasure_map[i][j]=0
            result = max(result,bfs(i,j))
print(result)

"""

시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	512 MB	18654	6376	4638	38.663%
문제
보물섬 지도를 발견한 후크 선장은 보물을 찾아나섰다.
보물섬 지도는 아래 그림과 같이 직사각형 모양이며 여러 칸으로 나뉘어져 있다.
각 칸은 육지(L)나 바다(W)로 표시되어 있다.
이 지도에서 이동은 상하좌우로 이웃한 육지로만 가능하며,
한 칸 이동하는데 한 시간이 걸린다.
보물은 서로 간에 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀있다.
육지를 나타내는 두 곳 사이를 최단 거리로 이동하려면 같은 곳을
두 번 이상 지나가거나, 멀리 돌아가서는 안 된다.

예를 들어 위와 같이 지도가 주어졌다면 보물은 아래 표시된 두 곳에 묻혀 있게 되고,
이 둘 사이의 최단 거리로 이동하는 시간은 8시간이 된다.

보물 지도가 주어질 때, 보물이 묻혀 있는 두 곳 간의 최단 거리로 이동하는 시간을 구하는 프로그램을 작성하시오.

입력
첫째 줄에는 보물 지도의 세로의 크기와 가로의 크기가 빈칸을 사이에 두고 주어진다.
이어 L과 W로 표시된 보물 지도가 아래의 예와 같이 주어지며, 각 문자 사이에는 빈 칸이 없다.
보물 지도의 가로, 세로의 크기는 각각 50이하이다.

출력
첫째 줄에 보물이 묻혀 있는 두 곳 사이를 최단 거리로 이동하는 시간을 출력한다.
"""