def DFS(N, cnt):
    global min_cnt
    if N == 1:
        if cnt < min_cnt:
            min_cnt = cnt
    else:
        if N % 3 == 0:
            DFS(N // 3, cnt+1)
        if N % 2 == 0:
            DFS(N // 2, cnt+1)
        DFS(N-1, cnt+1)

min_cnt = 100000
N = int(input())
DFS(N,0)
print(min_cnt)