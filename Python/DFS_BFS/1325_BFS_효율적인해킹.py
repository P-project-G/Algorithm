from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    queue = deque()
    queue.append(start)
    cnt = 0
    visit = [0]*(n+1)
    visit[start] = 1
    while queue:
        cur = queue.popleft()
        for acc in com[cur]:
            if visit[acc] == 0:
                visit[acc] = 1
                queue.append(acc)
                cnt+=1
    return cnt
n,m = map(int,input().split())
com = [ [] for _ in range (n+1) ]
for _ in range (m):
    a,b = map(int,input().split())
    com[b].append(a)

ans = []
for i in range (1,n+1):
    ans.append(bfs(i))

mx = max(ans)
answer = []
for i,v in enumerate(ans):
    if v == mx:
        answer.append(i+1)
print(*answer)

"""
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
5 초	256 MB	28220	5175	3417	20.484%

문제
해커 김지민은 잘 알려진 어느 회사를 해킹하려고 한다. 이 회사는 N개의 컴퓨터로 이루어져 있다. 김지민은 귀찮기 때문에, 한 번의 해킹으로 여러 개의 컴퓨터를 해킹 할 수 있는 컴퓨터를 해킹하려고 한다.

이 회사의 컴퓨터는 신뢰하는 관계와, 신뢰하지 않는 관계로 이루어져 있는데, A가 B를 신뢰하는 경우에는 B를 해킹하면, A도 해킹할 수 있다는 소리다.

이 회사의 컴퓨터의 신뢰하는 관계가 주어졌을 때, 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에, N과 M이 들어온다. N은 10,000보다 작거나 같은 자연수, M은 100,000보다 작거나 같은 자연수이다. 둘째 줄부터 M개의 줄에 신뢰하는 관계가 A B와 같은 형식으로 들어오며, "A가 B를 신뢰한다"를 의미한다. 컴퓨터는 1번부터 N번까지 번호가 하나씩 매겨져 있다.

출력
첫째 줄에, 김지민이 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 오름차순으로 출력한다.

예제 입력 1 
5 4
3 1
3 2
4 3
5 3

예제 출력 1 
1 2
"""