from collections import deque
import sys
input = sys.stdin.readline

def bfs(i):
    queue = deque()
    queue.append(i)
    color[i] = 1
    while queue:
        idx = queue.popleft()
        for go in graph[idx]:
            if color[go] == 0: # 방문하지 않았다면,
                color[go] = -color[idx] # 방문할 곳을 현재 정점과 다른 색상으로
                queue.append(go)
            else: # 방문했다면,
                if color[idx] == color[go]: # 현재 정점과 방문한 곳이 같은 색상이면 False
                    return False
    return True


K = int(input()) # 테스트 케이스의 개수 K (2<=K<=5)
for _ in range (K):
    # V: 1<=V<=20,000
    # E: 1<=E<=200,000
    V,E = map(int,input().split())
    graph = [ [] for _ in range (V+1) ] # 정점이 V개인 그래프 생성
    color = [0]*(V+1)
    is_True = True
    for _ in range (E):
        # E개의 간선 입력
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    for k in range (1,V+1):
        if color[k] == 0:
            if not bfs(k):
                is_True = False
                break
    print("YES" if is_True else "NO")

"""

시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	256 MB	42166	10805	6282	23.103%
문제
그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때, 그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.

그래프가 입력으로 주어졌을 때, 이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.

입력
입력은 여러 개의 테스트 케이스로 구성되어 있는데, 첫째 줄에 테스트 케이스의 개수 K(2≤K≤5)가 주어진다. 각 테스트 케이스의 첫째 줄에는 그래프의 정점의 개수 V(1≤V≤20,000)와 간선의 개수 E(1≤E≤200,000)가 빈 칸을 사이에 두고 순서대로 주어진다. 각 정점에는 1부터 V까지 차례로 번호가 붙어 있다. 이어서 둘째 줄부터 E개의 줄에 걸쳐 간선에 대한 정보가 주어지는데, 각 줄에 인접한 두 정점의 번호가 빈 칸을 사이에 두고 주어진다.

출력
K개의 줄에 걸쳐 입력으로 주어진 그래프가 이분 그래프이면 YES, 아니면 NO를 순서대로 출력한다.

예제 입력 1 
2
3 2
1 3
2 3
4 4
1 2
2 3
3 4
4 2

예제 출력 1 
YES
NO
"""