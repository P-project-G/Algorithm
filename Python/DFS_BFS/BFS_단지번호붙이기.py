"""
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	68645	27626	17557	38.533%

#2667
문제
<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을,
0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집들의 모임인 단지를 정의하고,
단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우,
혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다.
<그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고,
각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.



입력
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고,
그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

출력
첫 번째 줄에는 총 단지수를 출력하시오.
그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.


"""
from collections import deque

def bfs(i,j):
    queue=deque()
    queue.append((i,j))
    visit[i][j]=1
    cnt=0
    while queue:
        x,y=queue.popleft()
        cnt+=1
        for k in range (4):
            dx=x+col[k]
            dy=y+row[k]
            if 0<=dx<n and 0<=dy<n:
                if complex[dx][dy]==1 and visit[dx][dy]==0:
                    queue.append((dx,dy))
                    visit[dx][dy]=1
    return cnt

n=int(input())
complex=[list(map(int,input())) for _ in range(n)]
visit=[[0]*n for _ in complex]
col=[1,-1,0,0]
row=[0,0,1,-1]
answer=[]
for i in range(n):
    for j in range(n):
        if complex[i][j] == 1 and visit[i][j] == 0:
            answer.append(bfs(i,j))
print(len(answer))
for i in sorted(answer):
    print(i)