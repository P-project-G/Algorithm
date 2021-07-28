# https://www.acmicpc.net/problem/2526

import sys
input = sys.stdin.readline

n,p = map(int,input().split())

numArr = [0]*100000

next = n
cnt = 0
while True:
    next = (next*n)%p # next는 현재값 * n을 p로 나눈 나머지 값

    if next==0: # next가 0이라면, 반복되는 수는 0으로 고정
        break

    numArr[next] += 1 # 카운팅 방식으로 사이클 체크할 계획

    if numArr[next] == 2: # 2가 되는 순간이 사이클이 탄생했던 시점.
        numArr[next] -= 1
        break

if next == 0: # 0이면 반복되는 수의 숫자는 1이다.
    print(1)
else:
    answer = 0 # 반복되는 숫자 개수
    while True:
        next = (next*n)%p

        if numArr[next] == 2: # 또 다시 2가 되는 순간. 사이클의 총 개수이다
            break
        else:
            numArr[next]+=1
            answer += 1

    print(answer)