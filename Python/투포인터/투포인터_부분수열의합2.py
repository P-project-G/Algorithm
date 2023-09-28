from itertools import combinations
import sys
input = sys.stdin.readline

n,s = map(int,input().split())
arr = list(map(int,input().split()))

leftarr, rightarr = arr[:n//2], arr[n//2:] # 시간효율위해 리스트 2개로 분할
leftsum, rightsum = [], []  # 각각의 조합을 넣을 리스트

for i in range (n//2+1):
    left = list(combinations(leftarr,i)) # 조합생성
    for l in left: # 조합의 원소들을 합쳐서 리스트에 넣어준다.
        leftsum.append(sum(l))


for i in range (n-n//2+1):
    right = list(combinations(rightarr,i))
    for r in right:
        rightsum.append(sum(r))

# 조합의 원소들을 합친 리스트를 오름차순 정렬해준다.
leftsum.sort()
rightsum.sort()

answer = 0 # 정답 수

# 투포인터를 사용한다.
start,end = 0,len(rightsum)-1

#print(leftarr,rightarr)
#print(leftsum,rightsum)

while start < len(leftsum) and end >= 0:
    lv, rv = leftsum[start], rightsum[end]
    if lv+rv == s: # 두 값이 구하고자 하는 s와 같다면,
        Lcount, Rcount = 0,0
        while start < len(leftsum) and leftsum[start] == lv: # 현재값과 그 다음 값이 다를 때 까지 반복해준다.
            Lcount += 1 # 왼쪽의 수 증가
            start += 1 # 왼쪽 인덱스 1 증가

        while end >= 0 and rightsum[end] == rv:
            Rcount += 1 # 오른쪽 수 증가
            end -= 1 # 오른쪽 인덱스 1 감소

        answer += (Lcount * Rcount) # 경우의 수( [0,0] #2, [0,0,0] #3 이 있을 때 나올 수 있는 조합의 수는 6개다 )

    if lv+rv < s:
        start += 1
    if lv+rv > s:
        end -= 1

print(answer-1 if s==0 else answer) # 만약 구하고자 하는 값이 0이면 공집합을 제외해준다.

"""
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	10654	2344	1463	21.531%
문제
N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수의 개수를 나타내는 N과 정수 S가 주어진다. (1 ≤ N ≤ 40, |S| ≤ 1,000,000) 둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다. 주어지는 정수의 절댓값은 100,000을 넘지 않는다.

출력
첫째 줄에 합이 S가 되는 부분수열의 개수를 출력한다.

예제 입력 1 
5 0
-7 -3 -2 5 8

예제 출력 1 
1
"""