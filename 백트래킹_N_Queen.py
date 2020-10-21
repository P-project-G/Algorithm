"""
N_Queen 연습 [시간초과]
"""
def review(location,i,j):
    for col in range (N):
        if location[col][j]==True:
            return False
    for row in range (N):
        if location[i][row]==True:
            return False


    for plus_line in range (N):
        if i+plus_line >= N:
            continue
        if j+plus_line >= N:
            continue

        if location[i+plus_line][j+plus_line] == True:
            return False
    for plus_line2 in range (N):
        if i-plus_line2 < 0:
            continue
        if j-plus_line2 < 0:
            continue

        if location[i-plus_line2][j-plus_line2] == True:
            return False

    for minus_line in range (1,N):
        if i-minus_line < 0:
            continue
        if j+minus_line >= N:
            continue

        if location[i-minus_line][j+minus_line] == True:
            return False

    for minus_line2 in range (1,N):
        if i+minus_line2 >= N:
            continue
        if j-minus_line2 < 0:
            continue

        if location[i+minus_line2][j-minus_line2] == True:
            return False

    return True


def queen(depth):
    global answer
    if depth==N:
        answer+=1
        return

    for i in range (N):
        if True in location[i]:
            continue

        if i>0:
            if 1 not in location[i-1]:
                return

        for j in range (N):
            if True in location[i]:
                continue

            if review(location,i,j):
                location[i][j]=1
                queen(depth+1)
                location[i][j]=0

N=int(input())
answer=0
location=[[0]*N for _ in range (N)]

queen(0)
print(answer)