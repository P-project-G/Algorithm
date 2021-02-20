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