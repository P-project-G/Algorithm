import sys
input = sys.stdin.readline

#이분탐색, lower_bound 사용
def binarySearch(list,target):
    low,high = 0,n-1
    while (high-low)>0:
        mid = (low+high)//2

        if target > list[mid]:
            low = mid+1
        else:
            high = mid

    if list[high]==target:
        return high
    else:
        return -1

n,m = map(int,input().split())
arr1 = []
for _ in range (n):
    arr1.append(int(input()))

arr1.sort()

for _ in range (m):
    where = int(input())

    #이분탐색 적용
    print(binarySearch(arr1,where))

"""
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	512 MB	753	206	171	41.707%
문제
지훈이는 Sort 마스터다. 오랫동안 Sort 마스터 자리를 지켜온 지훈이는 이제 마스터 자리를 후계자에게 물려주려고 한다. 수많은 제자들 중에 후계자를 고르기 위해서 지훈이는 제자들에게 문제를 준비했다. 먼저 제자들에게 개의 원소를 가진 배열를 주고, 의 원소들이 오름차순으로 정렬된 배열를 만들게 한다. 그다음 개의 질문을 한다. 각 질문에는 정수 가 주어진다. 제자들은 주어진 정수가 에서 가장 먼저 등장한 위치를 출력하면 된다. 단, 가 에 존재하지 않는 경우에는 -1를 출력한다. Sort 마스터의 자리를 너무나도 물려받고 싶은 창국이를 위해 지훈이의 문제를 풀 수 있는 프로그램을 만들어 주자.

입력
첫째 줄에 배열의 원소의 개수 과 질문의 개수 이 공백으로 구분되어 주어진다.

다음 줄부터 줄에 걸쳐 정수 이 주어진다.

다음 줄부터 줄에 걸쳐 정수 가 주어진다.

출력
개의 질문에 대해서 주어진 가 에서 처음으로 등장한 위치를 출력한다. 단, 존재하지 않는다면 -1를 출력한다. (배열에서 가장 앞의 원소의 위치는 0이다.)

제한
1 ≤  ≤ 2×105
1 ≤  ≤ 2×105
-109 ≤  ≤ 109
-109 ≤  ≤ 109
예제 입력 1 
5 5
9
0
-1
3
2
-1
10
5
9
0

예제 출력 1 
0
-1
-1
4
1


예제 입력 2 
8 4
3
3
4
9
2
5
3
4
3
10
4
2
예제 출력 2 
1
-1
4
0
"""