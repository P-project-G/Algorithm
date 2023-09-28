"""
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	26436	7439	4948	26.234%

문제링크
https://www.acmicpc.net/problem/2573
"""
from collections import deque
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
q = deque()
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

for i in range(n):
    for j in range(m):
        if a[i][j] > 0:
            q.append((i, j))
        else:
            a[i][j] = -1

def bfs(i, j, check):
    bq = deque()
    bq.append((i, j))
    check[i][j] = True
    while bq:
        x, y = bq.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if check[nx][ny] is False and a[nx][ny] > 0:
                bq.append((nx, ny))
                check[nx][ny] = True

def counting():
    cnt = 0
    check = [[False]*m for _ in range(n)]
    for _ in range(len(q)):
        x, y = q.popleft()
        q.append((x, y))
        if check[x][y] is False:
            bfs(x, y, check)
            cnt += 1
            if cnt >= 2:
                return True
    return False

def melting():
    p = deque()
    for _ in range(len(q)):
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if a[x][y] > 0 and a[nx][ny] == -1:
                a[x][y] -= 1
        if a[x][y] > 0:
            q.append((x, y))
        elif a[x][y] == 0:
            p.append((x, y))
    while p:
        x, y = p.popleft()
        a[x][y] = -1

def solve():
    year = 0
    while q:
        melting()
        year += 1
        if counting() is True:
            return year
    return 0

print(solve())

