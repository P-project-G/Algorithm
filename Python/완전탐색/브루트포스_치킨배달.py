from collections import deque
import sys
input = sys.stdin.readline
from itertools import combinations

n,m = map(int,input().split())
townmap = [list(map(int,input().split())) for _ in range (n)]

house = []
chicken = []
mx = sys.maxsize
for i in range (n):
    for j in range (n):
        if townmap[i][j] == 1:
            house.append([i,j])
        if townmap[i][j] == 2:
            chicken.append([i,j])

dists = [list(map(lambda x: abs(x[0]-c[0])+abs(x[1]-c[1]),house)) for c in chicken]

for co in combinations((i for i in range(len(chicken))),m):
    candidate = sum(map(min,zip(*[dists[i] for i in co])))
#    print(list(zip(*[dists[i] for i in co])))
# zip함수로 2개씩 묶어 최소값 비교하기 키포인트

    if mx > candidate:
        mx = candidate

print(mx)



# 초안( 문제는 잘 통과했으나 시간으로 인해 위의 코드로 최적화 하였음 )
"""
from itertools import combinations
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
townmap = [list(map(int,input().split())) for _ in range (n)]

chicken = []
for i in range (n):
    for j in range (n):
        if townmap[i][j] == 2:
            chicken.append([i,j])

chicken = list(combinations(chicken,m))
result = []
mid_answer = []
answer = []
for chick in chicken:
    for i in range (n):
        for j in range (n):
            if townmap[i][j] == 1:
                result = []
                for c in chick:
                    result.append(abs(i - c[0]) + abs(j - c[1]))
                mid_answer.append(min(result))
    answer.append(mid_answer)
    mid_answer = []

print(min(map(sum,answer)))
"""