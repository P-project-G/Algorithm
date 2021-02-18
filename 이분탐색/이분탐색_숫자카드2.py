import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int,input().split()))
m = int(input())
card2 = list(map(int,input().split()))

card.sort()

answer = [0] * m
for cnt,i in enumerate(card2):
    low, high = 0, n
    while low <= high :
        mid = (low+high)//2
        if mid>-1 and mid<n:
            if card[mid] < i:
                low = mid+1
            else:
                high = mid-1
        else:
            break

    if mid>-1 and mid<n:
        answer[cnt]=card.count(i)

print(*answer)