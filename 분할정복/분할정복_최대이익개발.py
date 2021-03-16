import math
answer = [] # 값 확인용
def MaxValue(row,col,rn,cn):
    mx = 0
    for i in range (row,rn):
        for j in range (col,cn):
          if mx < toji[i][j]:
              mx = toji[i][j]
    return mx

def quadtree(row,col,rn,cn):
#    if row==rn and col==cn:
#        return 0
# 어차피 if rowMiddle != row랑 colMiddle != col에 걸려서 0이 리턴된다.

#    if len(answer)==math.log(n,2)*2: 선택한 값 확인용
#        print(answer,sum(answer))

    rowMiddle = (row+rn)//2
    colMiddle = (col+cn)//2
    a=b=c=d=0

    if rowMiddle != row:
#        answer.append(MaxValue(row,col,rowMiddle,cn))
        a=MaxValue(row,col,rowMiddle,cn)+quadtree(rowMiddle,col,rn,cn)
#        answer.pop()

#        answer.append(MaxValue(rowMiddle,col,rn,cn))
        b=MaxValue(rowMiddle,col,rn,cn)+quadtree(row,col,rowMiddle,cn)
#        answer.pop()
    if colMiddle != col:
#        answer.append(MaxValue(row,col,rn,colMiddle))
        c=MaxValue(row,col,rn,colMiddle)+quadtree(row,colMiddle,rn,cn)
#        answer.pop()

#        answer.append(MaxValue(row,colMiddle,rn,cn))
        d=MaxValue(row,colMiddle,rn,cn)+quadtree(row,col,rn,colMiddle)
#        answer.pop()

    iMax = a if a > b else b
    iMax = iMax if iMax > c else c
    iMax = iMax if iMax > d else d

    return iMax

#메인함수
n = int(input()) # 토지의 크기 n=2,4,8,16,32 중 하나
toji = [ list(map(int,input().split())) for _ in range (n) ]

print(quadtree(0,0,n,n))

"""
for i in range (n//2):
    for j in range (n):
        if mx<toji[i][j]:
            mx = toji[i][j]
quadtree(n//2, 0, n, n, 1, n,mx)

mx = 0
#하로 시작했을 때
for i in range (n//2,n):
    for j in range (n):
        if mx<toji[i][j]:
            mx = toji[i][j]
quadtree(0, 0, n//2, n, 1, n,mx)

mx = 0
#좌로 시작했을 때
for i in range (n):
    for j in range (n//2):
        if mx<toji[i][j]:
            mx = toji[i][j]
quadtree(0, n//2, n, n, 1, n,mx)

mx = 0
#우로 시작했을 때
for i in range (n):
    for j in range (n//2,n):
        if mx<toji[i][j]:
            mx = toji[i][j]
quadtree(0, 0, n, n//2, 1, n,mx)
"""

"""
토지개발
건형이는 가로 세로의 크기가 1로 이뤄진 작은 칸들이 모여 가로와 세로의 크기가 N인 N x N 크기의 토지를 개발하려 한다. (단, N은 2, 4, 8, 16, 32 중 하나이다) 토지의 각 칸에는 토지를 개발함으로써 얻을 수 있는 이익이 적혀 있으며, 토지는 아래와 같은 형태로 개발한다.

토지를 개발할 때에는 토지를 가로 혹은 세로 절반으로 나누어 한쪽 절반에 해당하는 부분을 모두 활용하여 개발해야 한다.
특정 부분을 모두 활용하여 개발할 때 얻을 수 있는 이익은, 해당 부분에서 개발로 얻을 수 있는 이익 중 최댓값이다.

각각의 선택지에 대하여 얻을 수 있는 이익은 해당 면적을 개발하여 얻을 수 있는 이익의 최댓값으로, 개발을 하고 난 이후에는 해당 면적을 더 개발하지 못하고, 남은 면적으로 반복하여 개발한다.

N x N 크기인 토지와 각각의 칸에 대한 이익이 주어질 때, 토지 개발을 통해 건형이가 얻을 수 있는 이익의 합 중 최댓값을 출력하시오.

입력
첫 번째 줄에 토지의 크기 N을 입력받는다.
N=2,4,8,16,32 중 하나
이후 N 개의 줄에 대하여 공백을 구분자로 개발을 통해 얻을 수 있는 이익을 입력받는다. (모든 이익은 양의 정수이다.)
1≦얻을 수 있는 이익≦100,000

출력
개발을 통해 건형이가 얻을 수 있는 이익의 합 중 최댓값을 출력한다.
이익의 합<=1,000,000

입력 예시
4
1 3 4 5
6 2 9 9
4 3 10 5
5 2 8 6

출력 예시
34
"""
