def DFS(d,idx,N,M):
    if d==M:
        print(*result)
        return
    for i in range (idx,N):
        if check[i]==True:
            print(check)
            continue


        check[i]=True
        result.append(i+1)

        DFS(d+1,i+1,N,M)

        result.pop()
        check[i]=False

N,M=map(int,input().split())
check=[False]*N
result=[]
DFS(0,0,N,M)