from heapq import heappush, heappop
import sys
input = sys.stdin.readline


# 프림 알고리즘 사용
def prim(s,v):
    heap = []
    visit = [0]*(v+1)
    visit[s]=1
    total = 0
    cnt = 1
    for a in graph[s]:
        heappush(heap,a)
    while heap:
        price, ver = heappop(heap)
        if visit[ver]==0:
            visit[ver]=1
            cnt += 1 # cnt 사용이유 : 시간을 단축하기 위하여.
            total += price
            for a in graph[ver]:
                heappush(heap,a)

        if cnt == v:
            return total
    return 0

#main
v,e = map(int,input().split())
graph = [ [] for _ in range (v+1) ]
for _ in range (e):
    a,b,c = map(int,input().split()) # a번 정점과 b번 정점이 가중치 c인 간선으로 연결
    graph[a].append([c,b])
    graph[b].append([c,a])
print(prim(1,v))