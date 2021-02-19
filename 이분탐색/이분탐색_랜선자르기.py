import sys
input = sys.stdin.readline

k,n = map(int,input().split())
lan = []
for i in range (k):
    lan.append(int(input()))

low,high = 0,1000000

while low <= high:
    mid = (low + high) // 2
    num = 0
    for i in lan:
        num += i//mid
    if num >= n:
        low = mid+1
    else:
        high = mid-1
print(high)