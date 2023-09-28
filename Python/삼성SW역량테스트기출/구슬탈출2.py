from collections import deque
import sys
input = sys.stdin.readline

# 기울었을 때 구슬의 움직임, 움직인 칸 수 리턴하는 함수
def move(v,h,dv,dh):
    c=0
    while board[v+dv][h+dh] != '#' and board[v][h] != 'O':
        v += dv
        h += dh
        c += 1
    return v,h,c


def bfs(rb,bb,d):
    queue = deque()
    queue.append([rb[0],rb[1], bb[0],bb[1], d])

    while queue:
        rv,rh,bv,bh,c = queue.popleft()
        if c > 10: # 10회가 넘으면 실패로 간주, -1 리턴
            return -1
        for k in range (4):
            drv,drh,rc = move(rv,rh,vertical[k],horizon[k])
            dbv,dbh,bc = move(bv,bh,vertical[k],horizon[k])
            if board[dbv][dbh] != 'O':
                if board[drv][drh] == 'O':
                    return c

                if drv==dbv and drh==dbh: # 만약 두 구슬의 위치가 같다면
                    if rc > bc: # rc가 더 높다면, 붉은 구슬이 더 많은 이동을 했다는 것, 즉 파란 구슬보다 뒤에 있었다는 것.
                        drv -= vertical[k]
                        drh -= horizon[k]
                    else:
                        dbv -= vertical[k]
                        dbh -= horizon[k]
                if visit[drv][drh][dbv][dbh] == 0:
                    visit[drv][drh][dbv][dbh]=1
                    queue.append([drv,drh,dbv,dbh,c+1])
    return -1

n,m = map(int,input().split())

board = [list(input().strip()) for _ in range(n)]
visit = [ [[[0]*m for _ in range (n)] for _ in range (m)] for _ in range (n) ]
vertical = [-1,1,0,0]
horizon = [0,0,-1,1]

for i in range (n):
    for j in range (m):
        if board[i][j] == 'R':
            r_bead = [i,j]
        if board[i][j] == 'B':
            b_bead = [i,j]

print(bfs(r_bead,b_bead,1))