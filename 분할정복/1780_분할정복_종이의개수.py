import sys
input = sys.stdin.readline

def ninetree(row,col,n):
    is_True = True
    color = paper[row][col]
    for i in range (row,row+n):
        if not is_True:
            break
        for j in range (col,col+n):
            if paper[i][j] != color:
                is_True = False
                for k in range(3):
                    for l in range (3):
                        ninetree(row+k*n//3, col+l*n//3, n//3)
                break

    if is_True == True:
        dict[color] += 1


n = int(input()) # 1 <= n <= 3**7  n은 3**k 꼴
paper = [ list(map(int,input().strip().split())) for _ in range (n) ]
dict = {-1:0, 0:0, 1:0}
ninetree(0,0,n)
for i,cnt in dict.items():
    print(cnt)

"""
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	256 MB	16164	9517	7201	59.209%

문제
N×N크기의 행렬로 표현되는 종이가 있다. 종이의 각 칸에는 -1, 0, 1의 세 값 중 하나가 저장되어 있다. 우리는 이 행렬을 적절한 크기로 자르려고 하는데, 이때 다음의 규칙에 따라 자르려고 한다.

만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다.
(1)이 아닌 경우에는 종이를 같은 크기의 9개의 종이로 자르고, 각각의 잘린 종이에 대해서 (1)의 과정을 반복한다.
이와 같이 종이를 잘랐을 때, -1로만 채워진 종이의 개수, 0으로만 채워진 종이의 개수, 1로만 채워진 종이의 개수를 구해내는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 37, N은 3k 꼴)이 주어진다. 다음 N개의 줄에는 N개의 정수로 행렬이 주어진다.

출력
첫째 줄에 -1로만 채워진 종이의 개수를, 둘째 줄에 0으로만 채워진 종이의 개수를, 셋째 줄에 1로만 채워진 종이의 개수를 출력한다.

예제 입력 1 
9
0 0 0 1 1 1 -1 -1 -1
0 0 0 1 1 1 -1 -1 -1
0 0 0 1 1 1 -1 -1 -1
1 1 1 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0
0 1 -1 0 1 -1 0 1 -1
0 -1 1 0 1 -1 0 1 -1
0 1 -1 1 0 -1 0 1 -1
예제 출력 1 
10
12
11
"""