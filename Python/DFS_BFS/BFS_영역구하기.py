from collections import deque
import sys
input = sys.stdin.readline

세로탐색 = [1,-1,0,0]
가로탐색 = [0,0,1,-1]

def bfs(i,j):
    모눈넓이 = 0
    큐 = deque()
    큐.append([i,j])

    while 큐:
        세로, 가로 = 큐.popleft()
        for k in range (4):
            큐_세로탐색 = 세로 + 세로탐색[k]
            큐_가로탐색 = 가로 + 가로탐색[k]
            if 큐_세로탐색 < 0 or 큐_가로탐색 < 0 or 큐_세로탐색 > m-1 or 큐_가로탐색 > n-1:
                continue
            if 방문[큐_세로탐색][큐_가로탐색] == 0 and 모눈종이[큐_세로탐색][큐_가로탐색] == 0:
                방문[큐_세로탐색][큐_가로탐색] = 1
                큐.append([큐_세로탐색,큐_가로탐색])
                모눈넓이+=1
    return 모눈넓이+1
m,n,k = map(int,input().split())
모눈종이 = [ [0]*n for _ in range (m) ]
직사각형 = []
for _ in range (k):
    직사각형.append(list(map(int,input().split())))

for i in 직사각형:
    x,y=[],[]
    while i:
        x.append(i.pop(0))
        y.append(i.pop(0))
    for i in range (m):
        for j in range (n):
            if m-y[1] <= i < m-y[0] and x[0] <= j < x[1]:
                모눈종이[i][j] = 1

방문 = [ [0]*n for _ in range (m) ]
cnt=0
넓이=[]
for i in range (m):
    for j in range (n):
        if 모눈종이[i][j] == 0 and 방문[i][j] == 0:
            방문[i][j] = 1
            넓이.append(bfs(i,j))
            cnt+=1
넓이.sort()
print(cnt)
print(*넓이)