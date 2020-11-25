def dfs(i,j):
    if visit[i][j]==0 and complex[i][j]==1:
        visit[i][j]=1
        answer[cnt]+=1
        if 1<=i<n and visit[i-1][j]==0:
            dfs(i-1,j)
        if 1<=j<n and visit[i][j-1]==0:
            dfs(i,j-1)
        if 0<=i<n-1 and visit[i+1][j]==0:
            dfs(i+1,j)
        if 0<=j<n-1 and visit[i][j+1]==0:
            dfs(i,j+1)


n=int(input())
complex=[list(map(int,input())) for i in range (n)]
visit=[[0]*n for _ in complex]
answer=[]
cnt=0
for i in range(n):
    for j in range(n):
        if visit[i][j]==0 and complex[i][j]==1:
            answer.append(0)
            dfs(i,j)
            cnt+=1
print(cnt)
for i in answer:
    print(i)