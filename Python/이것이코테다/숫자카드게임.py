N,M = map(int,input().split()) # N은 행, M은 열
card = [ list(map(int,input().split())) for _ in range (N) ]

# card를 lambda x : min(x)를 통해서 각 요소 별 최소값을 기준으로 내림차순 정렬한다.
# 그러면 가장 작은 값을 가진 요소가 0번째로 오게되고, 이 때 요소의 최소값을 구해주면 정답
print(min(sorted(card,key=lambda x: min(x),reverse=True)[0]))

"""
3 3
3 1 2
4 1 4
8 2 2
출력 : 2

2 4
7 3 1 8
3 3 3 4
출력 : 3
"""