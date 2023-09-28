def DFS(d,idx,N,M):
    if d==M:
        print(*result)
        return
    for i in range (idx-1,N):

        result.append(i+1)

        DFS(d+1,i+1,N,M)

        result.pop()

N,M=map(int,input().split())
result=[]
DFS(0,1,N,M)