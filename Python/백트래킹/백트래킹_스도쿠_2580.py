def review(x,y,i):
# 행에 존재하는가
    if i in sdoku[x]:
        return False
# 열에 존재하는가
    for col in range (9):
        if i == sdoku[col][y]:
            return False

# 3*3 구역에 존재하는가
    for n in range(3):
        for m in range(3):
            if i == sdoku[int(x / 3) * 3 + n][int(y / 3) * 3 + m]:
                return False

    return True

def DFS(depth):
    if depth==len(zero):
        for i in sdoku:
            print(*i)
        exit()
    else:
        idx_x = zero[depth][0]
        idx_y = zero[depth][1]

        for i in range (9):
            if review(idx_x,idx_y,i+1):
                sdoku[idx_x][idx_y]=(i+1)

                DFS(depth+1)

                sdoku[idx_x][idx_y]=0


sdoku=[list(map(int, input().split())) for _ in range (9)]
zero=[[x,y] for x in range (9) for y in range (9) if sdoku[x][y]==0]
DFS(0)