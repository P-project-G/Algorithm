"""
행 입력 후, 열을 입력 받는다.
6
0 1 1 0 0 0
0 1 1 0 1 1
0 0 0 0 1 1
0 0 0 0 1 1
1 1 0 0 1 0
1 1 1 0 0 0
6행, 6열 행열을 입력받았으면,
1이 차지하고 있는 공간의 개수와
공간의 넓이들을 출력하라.

위 예제에서 답은 (3개의 공간과 4, 7, 5의 넓이)

6
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 1 0 1 1
1 0 1 1 1
1 0 1 1 1

위 예제에서 답은 (4개의 공간과, 4,2,4,8의 넓이)
"""
from collections import deque
from sys import stdin

def bfs(i,j):
    queue=deque()
    queue.append((i,j))
    visit=[(i,j)]
    count = 0
    while queue:
        ii, jj = queue.popleft()

        count += 1
        graph[ii][jj] = 0
        for i in range(4):
            dii = ii + dx[i]
            djj = jj + dy[i]
            if dii>=0 and djj>=0 and dii<R and djj<C:
                if graph[dii][djj] == 1 and not (dii,djj) in visit:
                    queue.append((dii,djj))
                    visit.append((dii,djj))
    return count


n=int(stdin.readline())
graph = [ list(map(int,input().split())) for i in range (n) ]
x=[]

b=0
C=0
R=len(graph)
for i in graph[0]:
    C+=1

print(R,C)
dx=[1,-1,0,0]
dy=[0,0,1,-1]

for i in range(R):
    for j in range(C):
        if graph[i][j] == 1:
            x.append(bfs(i,j))
            b += 1
x.sort()
answer=[]
answer.append(b)
print(b,x)
print(answer)
for i in range (b):
    print(x[i], end=' ')