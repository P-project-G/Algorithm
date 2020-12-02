"""
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	71670	18574	8897	23.253%
문제
방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오.
단, 모든 간선의 가중치는 10 이하의 자연수이다.

입력
첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다.
(1≤V≤20,000, 1≤E≤300,000) 모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다.
둘째 줄에는 시작 정점의 번호 K(1≤K≤V)가 주어진다.
셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다.
이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다.
u와 v는 서로 다르며 w는 10 이하의 자연수이다.
서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.

출력
첫째 줄부터 V개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력한다.
시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 INF를 출력하면 된다.
"""
import sys
from heapq import heappush, heappop
inf = 100000000
v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
s = [[] for _ in range(v + 1)]
dp = [inf] * (v + 1)
heap = []

def dijkstra(start):
    dp[start] = 0
    heappush(heap, [0, start])
    while heap:
        w, n = heappop(heap)
        for n_n, wei in s[n]:
            n_w = wei + w
            if n_w < dp[n_n]:
                dp[n_n] = n_w
                heappush(heap, [n_w, n_n])

for i in range(e):
    u, v, w = map(int, sys.stdin.readline().split())
    s[u].append([v, w])
dijkstra(k)
print(dp)
for i in dp[1:]:
    print(i if i != inf else "INF")
"""
정답, 하지만 메모리부족으로 오답
from collections import deque
import sys
input = sys.stdin.readline

def bfs(k,i):
    if k==i:
        answer.append(0)
        return
    else:
        queue=deque()
        queue.append( (k,0) )
        while queue:
            x,edge = queue.popleft()

            if x==i:
                answer.append(edge)

            for id,di in graph[x]:
                if di != 0 :
                    queue.append( (id,edge+di) )


v,e=map(int, input().split())
k = int(input())
graph = [ [] for _ in range (v+1) ]
result=[]

for i in range (e):
    u,v,w = map(int, input().split())
    graph[u].append( (v,w) )

for i in range (v+1):
    answer=[]
    bfs(k,i+1)
    if answer:
        result.append(min(answer))
    else:
        result.append("INF")

for i in result:
    print(i)
"""