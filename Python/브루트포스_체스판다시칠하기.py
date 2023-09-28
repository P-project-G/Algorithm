"""
지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M*N 크기의 보드를 찾았다.
어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다.
지민이는 이 보드를 잘라서 8*8 크기의 체스판으로 만들려고 한다.

체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다.
구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고,
변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다.
따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다.
하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

보드가 체스판처럼 칠해져 있다는 보장이 없어서,
지민이는 8*8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다.
당연히 8*8 크기는 아무데서나 골라도 된다.
지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

- - - 예제 - - -
입력
10 13
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
WWWWWWWWWWBWB
WWWWWWWWWWBWB

출력
12

"""

def check(N,M,board):
    cnt=0
    for r in range (N,N+8): # N행을 시작으로, N+8행까지
        for c in range (M,M+8): # M열을 시작으로, M+8열까지
            # 첫 문자가 B라는 가정 하에 if문 작성
            if (r+c) % 2 == 1 and board[r][c] == 'B':
                cnt+=1
            if (r+c) % 2 == 0 and board[r][c] == 'W':
                cnt+=1
    answer.append(min(cnt,64-cnt)) # 첫 문자가 B라는 가정과, W라는 가정했을 때 비교해서 더 작은 값 추가

N,M=map(int,input().split()) # N행, M열
board=[input() for i in range (N)] # N행만큼 입력
answer=[]
for i in range (0,N-7): # 0행부터 N-7행까지
    for j in range (0,M-7): #0열부터 M-7열까지,
        check(i,j,board)

print(min(answer)) # 최종배열중 최솟값 출력