n = int(input())
n_card = list(map(int,input().split()))
m = int(input())
m_card = list(map(int,input().split()))

n_card.sort()

for i in m_card:
    low, high = 0, n
    while low <= high:
        mid = (low+high)//2
        if mid>-1 and mid<n:
            if n_card[mid] < i:
                low = mid+1
            else:
                high = mid-1
        else:
            break
    if mid>-1 and mid<n:
        if n_card[high+1] == i:
            print(1,end=" ")
        else:
            print(0,end=" ")
    else:
        print(0,end=" ")