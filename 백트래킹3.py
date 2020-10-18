def DFS(d,N,M):
    if d==M:
        print(*result)
        return
    for i in range (N):

        result.append(i+1)

        DFS(d+1,N,M)

        result.pop()

N,M=map(int,input().split())
result=[]
DFS(0,N,M)