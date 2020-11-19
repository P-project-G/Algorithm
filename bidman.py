import sys
N=int(sys.stdin.readline())
biz = [int(sys.stdin.readline()) for i in range (N)]
mx=max(biz)
total=sum(biz)-mx
if mx > total:
    print(mx-total)
else:
    if ( (mx+total) % 2 == 1):
        print(1)
    else:
        print(0)