from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    visit = [ [False]*l for _ in range (l) ]
    visit[start[0]][start[1]] = 1
    queue = deque()
    queue.append( [start[0],start[1]] )
    while True:
        v,h = queue.popleft()
        if v==end[0] and h==end[1]:
            return visit[v][h]-1
        for k in range (8):
            dv = v + vertical_move[k]
            dh = h + horizon_move[k]
            if dv<0 or dh<0 or dv>l-1 or dh>l-1:
                continue
            if visit[dv][dh]==0:
                visit[dv][dh]=visit[v][h]+1
                queue.append( [dv,dh] )

vertical_move = [1,2,1,2,-2,-1,-2,-1]
horizon_move = [-2,-1,2,1,-1,-2,1,2]

t = int(input())
for _ in range (t):
    l = int(input())
    start = list(map(int,input().split()))
    end = list(map(int,input().split()))
    print(bfs(start))