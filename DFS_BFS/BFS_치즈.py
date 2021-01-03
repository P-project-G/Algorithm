from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    큐 = deque()
    큐.append([0,0])
    치즈 = [ [-1]*가로 for _ in range (세로) ]
    치즈[0][0] = 0

    while 큐:
        큐_세로, 큐_가로 = 큐.popleft()
        for k in range (4):
            큐_세로탐색 = 큐_세로 + 세로탐색[k]
            큐_가로탐색 = 큐_가로 + 가로탐색[k]
            if 큐_세로탐색 < 0 or 큐_가로탐색 < 0 or 큐_세로탐색 > 세로-1 or 큐_가로탐색 > 가로-1:
                continue
            if 치즈[큐_세로탐색][큐_가로탐색] == -1:
                if 치즈배열[큐_세로탐색][큐_가로탐색] >= 1:
                    치즈배열[큐_세로탐색][큐_가로탐색] += 1
                else:
                    치즈[큐_세로탐색][큐_가로탐색] = 0
                    큐.append([큐_세로탐색,큐_가로탐색])



세로, 가로 = map(int,input().split())
치즈배열 = [ list(map(int,input().split())) for _ in range (세로) ]
세로탐색 = [1,-1,0,0]
가로탐색 = [0,0,1,-1]
방문 = [ [0]*가로 for _ in range (세로) ]


걸린시간 = 0
남은치즈개수 = []
while True:
    bfs()
    시간 = 0
    개수 = 0

    for i in range (세로):
        for j in range (가로):
            if 치즈배열[i][j] >= 2:
                치즈배열[i][j] = 0
                개수 +=1
                시간 = 1
    if 시간 == 1:
        걸린시간 += 1
        남은치즈개수.append(개수)
    else:
        break
print(걸린시간)
print(남은치즈개수.pop())

#그림포함문제
#링크 https://www.acmicpc.net/problem/2636
"""
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	9390	4595	3424	50.235%
"""
# BFS로 인접칸이 치즈면 치즈를 1증가, 공기칸이면 방문확인 후 이동
# 리스트 치즈배열에서 2이상인 것은 치즈가 녹았으니 0으로 바꾸고, 해당 시간에 녹인 치즈의 수를 구해 남은치즈개수 배열에 저장
# 치즈가 모두 녹을 때까지 반복.