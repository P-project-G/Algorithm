
def DFS(d,N,M):
    if d==M:
#        print(result)
        return
    for i in range (N):
        if check[i]==True:
            print(i,":check")
            continue

        check[i]=True
        result.append(i+1)

        DFS(d+1,N,M)

        result.pop()
        check[i]=False

if __name__=='__main__':
    N,M=map(int,input().split())
    check=[False]*N
    result=[]
    DFS(0,N,M)