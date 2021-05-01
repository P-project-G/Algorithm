import sys
from collections import deque
input = sys.stdin.readline

def bfs(node):
    queue = deque()
    queue.append(node)
    visit = [0]*(n+1)
    parent = [ [] for _ in range (n+1) ]
    while queue:
        nd = queue.popleft()
        for nod in tree[nd]:
            if visit[nod] == 0:
                visit[nod]=1
                queue.append(nod)
                parent[nod] = nd
    return parent
n = int(input())
tree = [ [] for _ in range (n+1) ]
for _ in range (n-1):
    p,c = map(int,input().split())
    tree[p].append(c)
    tree[c].append(p)
parent = bfs(1)

for i in range (2,n+1):
    print(parent[i])

"""
트리의 부모 찾기 성공분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	20564	8749	6510	43.351%

문제
루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

출력
첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.

예제 입력 1 
7
1 6
6 3
3 5
4 1
2 4
4 7
예제 출력 1 
4
6
1
3
1
4

예제 입력 2 
12
1 2
1 3
2 4
3 5
3 6
4 7
4 8
5 9
5 10
6 11
6 12
예제 출력 2 
1
1
2
3
3
4
4
5
5
6
6
출처
"""