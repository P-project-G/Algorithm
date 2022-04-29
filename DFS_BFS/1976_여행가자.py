def find(x):
    if (parent[x] != x):
        find(parent[x])

    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)

    if (a != b):
        if rank[a] > rank[b]:
            parent[b] = a
        else:
            parent[a] = b
            if (rank[a] == rank[b]):
                rank[b]+=1



def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)

    if a != b:
        if rank[a] > rank[b]:
            parent[b] = a
        else:
            parent[a] = b
            if rank[a] == rank[b]:
                rank[b] += 1



cityCnt = int(input())
planCity = int(input())

parent = [0]*(cityCnt+1)
rank = [0]*(cityCnt+1)
for i in range (1, cityCnt+1):
    parent[i] = i

for i in range (1,cityCnt+1):
    plan = list(map(int,input().split()))

    for p in range (len(plan)):
        if plan[p]:
            union(i,p+1)

travelPlan = list(map(int,input().split()))

temp = find(travelPlan[0])
answer = "YES"

for i in range (1,len(travelPlan)):
    if temp != find(travelPlan[i]):
        answer = "NO"
        break
print(answer)

