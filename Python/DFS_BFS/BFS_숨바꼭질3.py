from collections import deque
import sys
input = sys.stdin.readline

inf = sys.maxsize

def bfs(n,k):
    dp = [inf]*100001 # sys.maxsize로 10만1개의 리스트 생성
    queue = deque()
    queue.append([n,0]) # 큐에 현재 수빈의 위치 n과 그에 걸린 시간 0을 삽입
    dp[n] = 0 # dp[수빈 위치] = 0. 현재위치이기 때문에 0초이다.

    while queue:
        subin, t = queue.popleft() # 수빈의 위치와, 걸린 시간을 popleft
        if subin == k: # 만약 수빈의 위치가 동생의 위치 k와 같다면 return
            return dp[k] # 이때, return t를 해주어도 똑같음. k에 도달하기 까지의 최소값들 확인하기 위해 dp를 사용하였다.

        if subin*2 <= 100000 and dp[subin*2] > t:
            dp[subin*2] = t
            queue.append([subin*2,t])

        if subin+1 <= 100000 and dp[subin+1] > t+1:
            dp[subin+1] = t+1
            queue.append([subin+1,t+1])

        if subin-1 >= 0 and dp[subin-1] > t+1:
            dp[subin-1] = t+1
            queue.append([subin-1,t+1])


n,k = map(int,input().split())
print(bfs(n,k))

"""
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	512 MB	17963	5374	3353	26.805%
문제
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.
"""