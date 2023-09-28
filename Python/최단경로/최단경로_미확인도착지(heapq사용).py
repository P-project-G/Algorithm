from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def dijkstra(start): # 최단거리 알고리즘 사용
    dp = [sys.maxsize]*(n+1)
    dp[start] = 0
    heappush(heap,[start,0])

    while heap:
        vertex,weight = heappop(heap)
        for v,w in street[vertex]:
            if dp[v] > w+weight:
                dp[v] = w+weight
                heappush(heap,[v,w+weight])

    return dp

testcase = int(input().strip())


for _ in range(testcase):
    n, m, t = map(int, input().split()) # 교차로, 도로, 목적지 후보
    s, g, h = map(int, input().split()) # 출발지, 각 교차로
    street = [[] for _ in range(n+1)] # 그래프
    heap = []
    for _ in range (m):
        a,b,d = map(int,input().split())
        street[a].append([b,d]) # 방향성 X
        street[b].append([a,d])

    candidate = []
    for _ in range (t):
        candidate.append(int(input())) # 목적지 후보

    # 예술가들이 g와 h 사이의 도로를 건넜기 때문에 각각의 최단거리 구해줌
    s_ = dijkstra(s)
    g_ = dijkstra(g)
    h_ = dijkstra(h)

    answer = []
    for i in candidate:
        # 출발지로부터의 목적지까지 최단거리와 g,h사이의 도로를 경유했을 때의 최단거리가 같다면 정답에 추가.
        if s_[i] == (s_[g] + g_[h] + h_[i]) or s_[i] == (s_[h] + h_[g] + g_[i]):
            answer.append(i)
    answer.sort() # 오름차순 출력
    print(*answer)

"""
그림 포함

문제링크
https://www.acmicpc.net/problem/9370

시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
3 초	256 MB	7312	2034	1306	25.593%
문제
(취익)B100 요원, 요란한 옷차림을 한 서커스 예술가 한 쌍이 한 도시의 거리들을 이동하고 있다. 너의 임무는 그들이 어디로 가고 있는지 알아내는 것이다. 우리가 알아낸 것은 그들이 s지점에서 출발했다는 것, 그리고 목적지 후보들 중 하나가 그들의 목적지라는 것이다. 그들이 급한 상황이기 때문에 목적지까지 우회하지 않고 최단거리로 갈 것이라 확신한다. 이상이다. (취익)

어휴! (요란한 옷차림을 했을지도 모를) 듀오가 어디에도 보이지 않는다. 다행히도 당신은 후각이 개만큼 뛰어나다. 이 후각으로 그들이 g와 h 교차로 사이에 있는 도로를 지나갔다는 것을 알아냈다.

이 듀오는 대체 어디로 가고 있는 것일까?



예제 입력의 두 번째 케이스를 시각화한 것이다. 이 듀오는 회색 원에서 두 검은 원 중 하나로 가고 있고 점선으로 표시된 도로에서 냄새를 맡았다. 따라서 그들은 6으로 향하고 있다.

입력
첫 번째 줄에는 테스트 케이스의 T(1 ≤ T ≤ 100)가 주어진다. 각 테스트 케이스마다

첫 번째 줄에 3개의 정수 n, m, t (2 ≤ n ≤ 2 000, 1 ≤ m ≤ 50 000 and 1 ≤ t ≤ 100)가 주어진다. 각각 교차로, 도로, 목적지 후보의 개수이다.
두 번째 줄에 3개의 정수 s, g, h (1 ≤ s, g, h ≤ n)가 주어진다. s는 예술가들의 출발지이고, g, h는 문제 설명에 나와 있다. (g ≠ h)
그 다음 m개의 각 줄마다 3개의 정수 a, b, d (1 ≤ a < b ≤ n and 1 ≤ d ≤ 1 000)가 주어진다. a와 b 사이에 길이 d의 양방향 도로가 있다는 뜻이다.
그 다음 t개의 각 줄마다 정수 x가 주어지는데, t개의 목적지 후보들을 의미한다. 이 t개의 지점들은 서로 다른 위치이며 모두 s와 같지 않다.
교차로 사이에는 도로가 많아봐야 1개이다. m개의 줄 중에서 g와 h 사이의 도로를 나타낸 것이 존재한다. 또한 이 도로는 목적지 후보들 중 적어도 1개로 향하는 최단 경로의 일부이다.

출력
테스트 케이스마다

입력에서 주어진 목적지 후보들 중 불가능한 경우들을 제외한 목적지들을 공백으로 분리시킨 오름차순의 정수들로 출력한다.
예제 입력 1 
2
5 4 2
1 2 3
1 2 6
2 3 2
3 4 4
3 5 3
5
4
6 9 2
2 3 1
1 2 1
1 3 3
2 4 4
2 5 5
3 4 3
3 6 2
4 5 4
4 6 3
5 6 7
5
6

예제 출력 1 
4 5
6
"""