import sys
input = sys.stdin.readline

def divided(l,r):
    print()
    mid = (l+r)//2
    print('mid',mid,'l:',l,'r:',r)
    if l == r:
        return h[l]

    height = min(h[mid:mid+2])
    area = 2*height
    print('초기높이,넓이',height,area)

    left,right = mid,mid+1

    while l < left or right < r:
        print(left,right)
        if right < r and (left==l or h[left-1] < h[right+1]):
            right += 1
            height = min(height,h[right])
        else:
            left -= 1
            height = min(height,h[left])
        area = max(area,height*(right-left+1))
        print('area:',area,'height:',height,'right:',right,'left:',left)
    print('탐색후 가장넓은 건?',area)

    return max(divided(l,mid),divided(mid+1,right),area)

#main
while True:
    h = list(map(int,input().split()))
    length = h.pop(0)

    if length == 0:
        break
    print(divided(0,length-1))