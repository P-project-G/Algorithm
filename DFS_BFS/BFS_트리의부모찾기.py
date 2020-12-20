from collections import deque
import sys
input = sys.stdin.readline


def bfs(start):
    visit = [False]*(n+1)
    queue=deque()
    queue.append(start)
    visit[start]=True

    while queue:
        cur = queue.popleft()
        for i in s[cur]:
            if visit[i] == False:
                visit[i] = True
                parent[i] = cur
                queue.append(i)
n=int(input())
parent=[ [] for _ in range (n+1) ]
s=[ [] for _ in range (n+1) ]
for i in range (n-1):
    a,b=map(int,input().split())
    s[b].append(a)
    s[a].append(b)
answer=[]
bfs(1)
for i in range (2,n+1):
    print(parent[i])

"""
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	15962	6714	5037	43.911%
문제
루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

출력
첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.


"""