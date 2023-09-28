import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
def preorder(lin,rin,lpo,rpo):
    if lin > rin or lpo > rpo:
        return
    parent = posto[rpo] # 후위순회에서 부모노드 찾기
    print(parent,end=' ')
    l = idx[parent] - lin # 왼쪽인자 갯수
    r = rin - idx[parent] # 오른쪽인자 갯수
    preorder(lin,lin+l-1, lpo,lpo+l-1)
    preorder(rin-r+1,rin, rpo-r,rpo-1)


n=int(input())
ino = list(map(int,input().split()))
posto = list(map(int,input().split()))
idx = [0]*(n+1)
for i in range (n):
    idx[ino[i]] = i
preorder(0,n-1,0,n-1)