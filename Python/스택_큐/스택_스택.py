import sys
input = sys.stdin.readline
N=int(input())

cmd = [ input().split() for i in range (N) ]
stack = []
for i in cmd:
    if i[0]=="push":
        stack.append(i[1])
    if i[0]=="pop":
        if stack != []:
            print(stack.pop())
        else:
            print(-1)
    if i[0]=="size":
        print(len(stack))
    if i[0]=="empty":
        if stack:
            print(0)
        else:
            print(1)
    if i[0]=="top":
        if stack != []:
            print(stack[-1])
        else:
            print(-1)