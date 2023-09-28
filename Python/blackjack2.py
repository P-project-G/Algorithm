from itertools import combinations
N,M=map(int,input().split())
card=list(map(int,input().split()))
cardset=list(map(sum,combinations(card,3)))
mxcard=min(cardset)
for i in cardset:
    if mxcard<i<=M:
        mxcard=i

print(cardset)
print(mxcard)