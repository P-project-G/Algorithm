from heapq import heappush,heappop
import sys
input = sys.stdin.readline

def find(x):
    if x != parent[x]:
        return find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)

    if a > b :
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
xlanet = []
ylanet = []
zlanet = []

for i in range (n):
    x,y,z = map(int,input().split())
    xlanet.append([x,i])
    ylanet.append([y,i])
    zlanet.append([z,i])
xlanet.sort()
ylanet.sort()
zlanet.sort()

tunnel = []
for i in range (n-1):
    tunnel.append((abs(xlanet[i][0]-xlanet[i+1][0]),xlanet[i][1],xlanet[i+1][1]))
    tunnel.append((abs(ylanet[i][0]-ylanet[i+1][0]),ylanet[i][1],ylanet[i+1][1]))
    tunnel.append((abs(zlanet[i][0]-zlanet[i+1][0]),zlanet[i][1],zlanet[i+1][1]))
tunnel.sort()
parent = [i for i in range (n)]
cost = 0
while tunnel:
    c,a,b = heappop(tunnel)
    if find(a) != find(b):
        union(a,b)
        cost += c
print(cost)


"""
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	8457	3145	2217	36.072%

문제
때는 2040년, 이민혁은 우주에 자신만의 왕국을 만들었다. 왕국은 N개의 행성으로 이루어져 있다. 민혁이는 이 행성을 효율적으로 지배하기 위해서 행성을 연결하는 터널을 만들려고 한다.

행성은 3차원 좌표위의 한 점으로 생각하면 된다. 두 행성 A(xA, yA, zA)와 B(xB, yB, zB)를 터널로 연결할 때 드는 비용은 min(|xA-xB|, |yA-yB|, |zA-zB|)이다.

민혁이는 터널을 총 N-1개 건설해서 모든 행성이 서로 연결되게 하려고 한다. 이때, 모든 행성을 터널로 연결하는데 필요한 최소 비용을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 행성의 개수 N이 주어진다. (1 ≤ N ≤ 100,000) 다음 N개 줄에는 각 행성의 x, y, z좌표가 주어진다. 좌표는 -109보다 크거나 같고, 109보다 작거나 같은 정수이다. 한 위치에 행성이 두 개 이상 있는 경우는 없다. 

출력
첫째 줄에 모든 행성을 터널로 연결하는데 필요한 최소 비용을 출력한다.

예제 입력 1 
5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19
예제 출력 1 
4
"""