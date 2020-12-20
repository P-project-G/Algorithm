"""
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
3 초	512 MB	34831	16972	11018	45.809%
문제
방향 없는 그래프가 주어졌을 때,
연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2)
둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v)
같은 간선은 한 번만 주어진다.

출력
첫째 줄에 연결 요소의 개수를 출력한다.
"""

from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    queue = deque()
    queue.append(start)
    visit[start] = True

    while queue:
        a = queue.popleft()
        for i in s[a]:
            if visit[i]==False:
                visit[i]=True
                queue.append(i)

n,m = map(int, input().split())
s = [ [] for _ in range (n+1) ]
visit = [ False for _ in range (n+1) ]
cnt=0

for i in range (m):
    start, arrival = map(int, input().split())
    s[start].append(arrival)
    s[arrival].append(start)

for i in range (1,n+1):
    if not visit[i]:
        bfs(i)
        cnt+=1
print(cnt)