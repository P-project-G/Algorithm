from collections import deque
import sys
input = sys.stdin.readline

# 펑션
def bfs():
    global fire_queue, person_queue
    while person_queue:
        temp = deque()
        while person_queue:
            vv,hh = person_queue.popleft()
            if (vv == h-1 or hh == w-1 or vv == 0 or hh == 0) and building[vv][hh] != '*':
                return building[vv][hh]+1
            for k in range (4):
                dv = vv + search_v[k]
                dh = hh + search_h[k]
                if dv<0 or dh<0 or dv>h-1 or dh>w-1:
                    continue

                if building[dv][dh] == '.' and building[vv][hh] != '*':
                    building[dv][dh] = building[vv][hh]+1
                    temp.append([dv,dh])
        person_queue = temp
        temp = deque()

        while fire_queue:
            vv,hh = fire_queue.popleft()
            for k in range (4):
                dv = vv + search_v[k]
                dh = hh + search_h[k]
                if dv<0 or dh<0 or dv>h-1 or dh>w-1:
                    continue

                if visit[dv][dh] == 0 and building[dv][dh] != '#':
                    visit[dv][dh] = 1
                    building[dv][dh] = '*'
                    temp.append([dv,dh])
        fire_queue = temp
    return 'IMPOSSIBLE'


# main
search_v = [1,-1,0,0]
search_h = [0,0,-1,1]

TEST_CASE = int(input().strip())

for _ in range (TEST_CASE):
    person_queue, fire_queue = deque(), deque()
    w,h = map(int,input().split())
    visit = [ [0]*w for _ in range (h) ]
    building = [ list(input().strip()) for _ in range (h) ]
    for i in range (h):
        for j in range (w):
            if building[i][j] == '@':
                building[i][j] = 0
                person_queue.append([i,j])
            if building[i][j] == '*':
                visit[i][j] = 1
                fire_queue.append([i,j])
    print(bfs())

"""
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	19484	4729	2924	22.214%
문제
상근이는 빈 공간과 벽으로 이루어진 건물에 갇혀있다. 건물의 일부에는 불이 났고, 상근이는 출구를 향해 뛰고 있다.

매 초마다, 불은 동서남북 방향으로 인접한 빈 공간으로 퍼져나간다. 벽에는 불이 붙지 않는다. 상근이는 동서남북 인접한 칸으로 이동할 수 있으며, 1초가 걸린다. 상근이는 벽을 통과할 수 없고, 불이 옮겨진 칸 또는 이제 불이 붙으려는 칸으로 이동할 수 없다. 상근이가 있는 칸에 불이 옮겨옴과 동시에 다른 칸으로 이동할 수 있다.

빌딩의 지도가 주어졌을 때, 얼마나 빨리 빌딩을 탈출할 수 있는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수가 주어진다. 테스트 케이스는 최대 100개이다.

각 테스트 케이스의 첫째 줄에는 빌딩 지도의 너비와 높이 w와 h가 주어진다. (1 ≤ w,h ≤ 1000)

다음 h개 줄에는 w개의 문자, 빌딩의 지도가 주어진다.

'.': 빈 공간
'#': 벽
'@': 상근이의 시작 위치
'*': 불
각 지도에 @의 개수는 하나이다.

출력
각 테스트 케이스마다 빌딩을 탈출하는데 가장 빠른 시간을 출력한다. 빌딩을 탈출할 수 없는 경우에는 "IMPOSSIBLE"을 출력한다.
"""