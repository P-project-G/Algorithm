import sys
input = sys.stdin.readline
def dfs(i,j,s):
    global answer
    if i == n - 1 and j == n - 1: answer += 1
    if s == 0:
        if j + 1 < n and p[i][j + 1] == 0: dfs(i, j + 1, 0)
        if i + 1 < n and j + 1 < n:
            if p[i][j + 1] == 0 and p[i + 1][j] == 0 and p[i + 1][j + 1] == 0:
                dfs(i + 1, j + 1, 2)
    elif s == 1:
        if i + 1 < n and p[i + 1][j] == 0: dfs(i + 1, j, 1)
        if i + 1 < n and j + 1 < n:
            if p[i][j + 1] == 0 and p[i + 1][j] == 0 and p[i + 1][j + 1] == 0:
                dfs(i + 1, j + 1, 2)
    elif s == 2:
        if i + 1 < n and p[i + 1][j] == 0: dfs(i + 1, j, 1)
        if j + 1 < n and p[i][j + 1] == 0: dfs(i, j + 1, 0)
        if i + 1 < n and j + 1 < n:
            if p[i][j + 1] == 0 and p[i + 1][j] == 0 and p[i + 1][j + 1] == 0:
                dfs(i + 1, j + 1, 2)
n = int(input()) # 집의 크기 n (3 <= n <= 16)
p = [list(map(int,input().split())) for k in range(n)]
answer = 0
#DFS 3번째 인자는 상태로 0은가로 1은세로 2는대각선상태
dfs(0,1,0)
print(answer)