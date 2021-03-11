from heapq import heappush,heappop
import sys
input = sys.stdin.readline

n,m = map(int,input().split()) # 우주신의 개수 n , 이미 연결된 통로의 개수 m

#크루스칼 유니온,파인드
def find(x):
    if parent[x] != x:
        return find(parent[x])

    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)

    if rank[a] > rank[b]:
        parent[b] = a
    else:
        parent[a] = b
        if rank[a] == rank[b]:
            rank[b] += 1

gatexy = []
heap = []

parent = [ i for i in range (n) ]
rank = [0] * n
cost = 0
for _ in range (n):
    x,y=map(int,input().split())
    gatexy.append([x,y])

for _ in range (m):
    a,b = map(int,input().split())
    a-=1
    b-=1
    if find(a) != find(b):
        res = (abs(gatexy[a][0] - gatexy[b][0])**2 + abs(gatexy[a][1]-gatexy[b][1])**2)**0.5
        union(a,b)


for i in range (n-1):
    for j in range (i+1,n):
        res = (abs(gatexy[i][0] - gatexy[j][0]) ** 2 + abs(gatexy[i][1] - gatexy[j][1]) ** 2) ** 0.5
        heappush(heap,[res,i,j])


while heap:
    c,i,j = heappop(heap)
    if find(i) != find(j):
        union(i,j)
        cost += c

print(format(cost,"0.2f"))