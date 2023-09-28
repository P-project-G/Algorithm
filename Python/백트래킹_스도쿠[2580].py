"""
스도쿠는 18세기 스위스 수학자가 만든 '라틴 사각형'이랑 퍼즐에서 유래한 것으로 현재 많은 인기를 누리고 있다.
이 게임은 아래 그림과 같이 가로, 세로 각각 9개씩 총 81개의 작은 칸으로 이루어진 정사각형 판 위에서 이뤄지는데,
게임 시작 전 일부 칸에는 1부터 9까지의 숫자 중 하나가 쓰여 있다.

게임 시작 전 스도쿠 판에 쓰여 있는 숫자들의 정보가 주어질 때 모든 빈 칸이 채워진 최종 모습을 출력하는 프로그램을 작성하시오.

입력
아홉 줄에 걸쳐 한 줄에 9개씩 게임 시작 전 스도쿠판 각 줄에 쓰여 있는 숫자가 한 칸씩 띄워서 차례로 주어진다.
스도쿠 판의 빈 칸의 경우에는 0이 주어진다. 스도쿠 판을 규칙대로 채울 수 없는 경우의 입력은 주어지지 않는다.

출력
모든 빈 칸이 채워진 스도쿠 판의 최종 모습을 아홉 줄에 걸쳐 한 줄에 9개씩 한 칸씩 띄워서 출력한다.

스도쿠 판을 채우는 방법이 여럿인 경우는 그 중 하나만을 출력한다.
"""




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