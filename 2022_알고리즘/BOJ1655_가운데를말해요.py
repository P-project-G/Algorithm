import sys
input = sys.stdin.readline

import heapq

n = int(input())
ans = []
cnt = 0
leftHeap = []
rightHeap = []
for i in range (n):
    num = int(input())

    # 왼쪽 힙(최대), 오른쪽 힙(최소) 구성 후
    # 같으면 최대힙에, 다르면 최소힙에 추가
    # 항상 최대힙의 0번째 인덱스가 중간 값이 되기 위함
    if (len(leftHeap) == len(rightHeap)):
        heapq.heappush(leftHeap, -num)
    else:
        heapq.heappush(rightHeap, num)


    if rightHeap and leftHeap[0]*-1 > rightHeap[0]:
        lValue = heapq.heappop(leftHeap) * -1
        rValue = heapq.heappop(rightHeap)

        heapq.heappush(leftHeap, -rValue)
        heapq.heappush(rightHeap, lValue)

    print(-leftHeap[0])