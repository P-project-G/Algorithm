"""
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를
서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.
"""
def solution(row):
    global answer # answer를 메인함수의 answer와 공용으로 사용
    if row==N:
        answer+=1
        return

    for col in range (N):

        if not (checkVertical[col] or checkPslash[row+col] or checkMslash[row-col+N-1]):
            checkVertical[col] = checkPslash[row+col] = checkMslash[row-col+N-1] = True
            solution(row+1)
            checkVertical[col] = checkPslash[row + col] = checkMslash[row - col + N - 1] = False

if __name__=='__main__':
    N=int(input()) # N*N 체스판의 N
    answer=0 # 퀸을 놓은 개수

    #수직선 개수, 우상향대각선 개수, 좌상향대각선 체크
    checkVertical, checkPslash, checkMslash = [False]*N, [False]*(2*N-1), [False]*(2*N-1)

    solution(0)
    print(answer)

    if not (True or False or False):
        print("false")
