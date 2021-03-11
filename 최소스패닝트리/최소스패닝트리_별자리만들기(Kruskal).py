from heapq import heappush,heappop
import sys
input = sys.stdin.readline

#union
def union(a,b):
    a=find(a)
    b=find(b)

    if a != b:
        if rank[a] > rank[b]:
            parent[b] = a
        else:
            parent[a] = b
            if rank[a] == rank[b]:
                rank[b] += 1


#find
def find(x): # 부모노드를 찾을 때 가지 재귀
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]


#main
n = int(input())

stars=[]
graph = []

for _ in range (n):
    x,y=map(float,input().split())
    stars.append([x,y])

for i in range (n-1):
    for j in range (i+1,n):
        res=(abs(stars[i][0]-stars[j][0])**2+abs(stars[i][1]-stars[j][1])**2)**0.5
        heappush(graph,[res,i,j])

parent = [ i for i in range (n) ]
rank = [0]*n
cost = 0

while graph:
    c,i,j = heappop(graph)
    if find(i) != find(j):
        cost += c
        union(i,j)


print(format(cost,"0.2f"))

"""
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	3981	2104	1694	53.220%
문제
도현이는 우주의 신이다. 이제 도현이는 아무렇게나 널브러져 있는 n개의 별들을 이어서 별자리를 하나 만들 것이다. 별자리의 조건은 다음과 같다.

별자리를 이루는 선은 서로 다른 두 별을 일직선으로 이은 형태이다.
모든 별들은 별자리 위의 선을 통해 서로 직/간접적으로 이어져 있어야 한다.
별들이 2차원 평면 위에 놓여 있다. 선을 하나 이을 때마다 두 별 사이의 거리만큼의 비용이 든다고 할 때, 별자리를 만드는 최소 비용을 구하시오.

입력
첫째 줄에 별의 개수 n이 주어진다. (1 ≤ n ≤ 100)

둘째 줄부터 n개의 줄에 걸쳐 각 별의 x, y좌표가 실수 형태로 주어지며, 최대 소수점 둘째자리까지 주어진다. 좌표는 1000을 넘지 않는 양의 실수이다.

출력
첫째 줄에 정답을 출력한다. 절대/상대 오차는 10-2까지 허용한다.

예제 입력 1 
3
1.0 1.0
2.0 2.0
2.0 4.0

예제 출력 1 
3.41
"""