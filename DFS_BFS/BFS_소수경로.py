from collections import deque
import sys
input = sys.stdin.readline

### --- 함수
# 소수판별
def is_prime(n):
    return all( [(n%j) for j in range(2, int(n**0.5)+1)] ) and n>1

# BFS
def bfs(start,end):
    visit = [0]*10000
    visit[start] = 1
    queue = deque()
    queue.append([start,0])

    while queue:
        num,cnt = queue.popleft()
        if num == end:
            return cnt

        if num < 1000:
            continue

        # 1의자리부터 1000의자리를 각각 바꿔주며 소수인 것을 큐에 넣어줌
        for i in [1,10,100,1000]:
            n = num - num % (i*10) // i*i # num=1033일 때, n은 각각 1030, 1033, 1033, 1033이 된다.
            for j in range (10):
                if visit[n] == 0 and num_arr[n]: # n에 방문하지 않았고, n이 소수라면
                    visit[n] = 1
                    queue.append( [n, cnt+1] )
                n += i

### --- main
T = int(input())
num_arr = [ True for i in range (10001) ] # 소수는 True인 배열
for i in range(10000):
    if not is_prime(i):
        num_arr[i] = False

for _ in range (T):
    start,end = map(int,input().split())
    answer = bfs(start,end)

    if answer == None:
        print("Impossible")
    else:
        print(answer)
