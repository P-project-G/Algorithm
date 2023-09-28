K=int(input())

n = [int(input()) for i in range (K)]
stack = []
for i in n:
    if i != 0 :
        stack.append(i)
    else:
        stack.pop()
print(sum(stack))